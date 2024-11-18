from django.db import models

# Create your models here.
import qrcode
from io import BytesIO
import os
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw

class CardOwner(models.Model):
    card_uid = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    qr_img = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.card_uid})"
    

    def generate_card_uid(self):
        """Generate a unique card UID if not provided."""
        if not self.card_uid:
            self.card_uid = str(uuid.uuid4())

    def generate_qr_code(self):
        """Generate a QR code based on the card owner's details."""
        qr_data = f"Name: {self.name} Email: {self.email} Phone: {self.phone} Hostel: {self.hostel_name} Room: {self.room_number}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Lower error correction
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code to the model's `qr_img` field
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f"{self.name}_{self.card_uid}_qr.png"
        self.qr_img.save(file_name, ContentFile(buffer.getvalue()), save=False)

    def save(self, *args, **kwargs):
        """Call both helper methods before saving the model."""
        self.generate_card_uid()
        self.generate_qr_code()
        super().save(*args, **kwargs)