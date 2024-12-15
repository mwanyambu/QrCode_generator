from django.contrib import admin
from django.urls import path, include
from scan import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Welcome page route
    path('', views.add_card, name='add_card'),  # Root URL points to add_card
    path('scan/', include('scan.urls')),  # Add a 'scan/' prefix for scan app URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)