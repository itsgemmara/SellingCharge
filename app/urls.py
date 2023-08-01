from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns for your views...
    path('seller/increase_credit/<int:seller_id>', views.increase_credit, name='increase_credit'),
    # Other URL patterns for your views...
]