from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothng in your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J6dsDIxAfU6TjYmTZt4Ut4We49olxBAdp5W0uQbQo6k7fctzC3j67U95wW7vBluRF7uQF0wjx1fA4hvExPeG1Ao00oXLKWPzW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    