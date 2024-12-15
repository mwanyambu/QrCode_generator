from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Welcome page route
    path('add_card/', views.add_card, name='add_card'),
]