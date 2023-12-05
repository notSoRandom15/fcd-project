from django.urls import path

from fcp.billing.views import billing, checkout_session


app_name = 'billing'
urlpatterns = [
    path('', billing, name='home'),
    path('checkout', view=checkout_session, name='checkout'),
]
