from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from product.models import product
# Create your models here.

#order
class order(models.Model):
    statusList=[('Pending', 'Pending'),
                ('Delivered', 'Delivered'),
                ('Returned)', 'Returned)'),
                ]
    product=models.ForeignKey(product, on_delete=models.SET_DEFAULT, default='Deleted')
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    # price=models.PositiveIntegerField()
    qntt=models.PositiveIntegerField(default=1)
    # fullName=models.CharField(max_length=20)
    # mobile=models.CharField(max_length=20)
    # address=models.CharField(max_length=100)
    orderedDate=models.DateField(default=datetime.now)
    status=models.CharField(max_length=20, choices=statusList, default='Pending')

    # def total(self):
    #     return self.price * self.qntt

    def saveOrder(self):
        self.save()

    def __str__(self):
        return f"{self.customer.username}'s order"

    def statusOption(self):
            if (self.status=='0'):
                return 'Pending'
            else:
                return self.status