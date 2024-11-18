from django.contrib import admin
from .models import CardOwner
import uuid

@admin.register(CardOwner)
class CardOwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'card_uid', 'created']
    readonly_fields = ['card_uid']  # Make card_uid read-only to prevent changes

    def save_model(self, request, obj, form, change):
        # Ensure card_uid is generated manually during admin save
        if not obj.card_uid:
            obj.card_uid = str(uuid.uuid4())
        super().save_model(request, obj, form, change)