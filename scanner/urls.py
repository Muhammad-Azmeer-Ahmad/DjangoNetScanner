from django.urls import path
from scanner.views import index, scan_target

urlpatterns = [
    path('', index, name='index'),
    path('scan/', scan_target, name='scan'),
]
