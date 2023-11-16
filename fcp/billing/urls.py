from django.urls import path

from fcp.billing.views import billing


app_name = 'billing'
urlpatterns = [
    path('', billing, name='home'),
]
