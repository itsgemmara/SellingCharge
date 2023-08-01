import logging
import datetime
from decimal import Decimal     
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from .validators import validate_phone_number

logger = logging.getLogger(__name__)


class InsufficientCreditException(Exception):
    pass


class Profile(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=13, null=True, unique=True, validators=[validate_phone_number])
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.phone_number
    

class Seller(Profile):
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def increase_credit(self, amount):
        try: 
            self.credit += amount
            self.save()
        except:
            raise InsufficientCreditException(f"""
                Insufficient credit for seller {self.phone_number} to perform charge sale.
                Available Credit: {self.credit}, Required Amount: {amount}
                """)
        Transaction.objects.create(
            seller=self,
            transaction_type='increase',
            amount=amount
        )
        logger.info(f"Credit increased for seller {self.phone_number} | Amount: {amount} | {datetime.datetime.now()}")

    def charge_sale(self, amount):
        if self.credit >= amount:
            self.credit -= amount
            self.save()
            Transaction.objects.create(
                seller=self,
                transaction_type='charge',
                amount=amount
            )
            logger.info(f"Charge sale for seller {self.phone_number} | Amount: {amount} | {datetime.datetime.now()}")
        else:
            logger.warning(f"Insufficient credit for seller {self.phone_number} to perform charge sale | Amount: {amount} | {datetime.datetime.now()}")
            raise InsufficientCreditException(f"""
                Insufficient credit for seller {self.phone_number} to perform charge sale.
                Available Credit: {self.credit}, Required Amount: {amount}
                """)

    class Meta:
        verbose_name = 'Seller'  
        verbose_name_plural = 'Sellers'


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('increase', 'Increase Credit'),
        ('charge', 'Charge Sale'),
    )

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.seller.phone_number} - Amount: {self.amount}"
\
    class Meta:
        verbose_name = 'Transaction'  
        verbose_name_plural = 'Transactions'
