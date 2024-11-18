from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CardOwner
from .forms import CardOwnerForm


# Create your views here.
def add_card(request):
    if request.method == 'POST':
        form = CardOwnerForm(request.POST)
        if form.is_valid():
            card_owner = form.save()
            return HttpResponse(f"Card added successfully. QR Code: <img src='{card_owner.qr_img.url}' />")          
    else:
        form = CardOwnerForm()
    return render(request, 'add_card.html', {'form': form})