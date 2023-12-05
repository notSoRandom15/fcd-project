import stripe
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect


# Create your views here.

def billing(request):
    return render(request, 'billing/billing_home.html')


def checkout_session(request:HttpRequest):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            currency='eur',
            mode='setup',
            success_url='http://localhost:4242/success',
            cancel_url='http://localhost:4242/cancel',
  )

        return redirect(session.url, code=303)
    
    return render(request, 'billing/checkout_session.html')