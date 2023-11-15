from django.urls import path

from fcp.billing.views import billing



urlpatterns = [
    path('', billing, name='billing'),
]
