from decimal import Decimal   
from django.shortcuts import get_object_or_404
from .models import Seller, Profile
from django.http import HttpResponse


def increase_credit(request, seller_id):
    # Get the seller object based on the seller_id from the URL
    seller = get_object_or_404(Seller, pk=seller_id)

    if request.method == 'GET':
        # Get the credit amount to increase from the form data
        amount = Decimal(request.POST.get('credit_amount', 4))
        seller.increase_credit(amount)
    return HttpResponse('done')