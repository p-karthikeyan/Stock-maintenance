from django.db import models
from django.contrib.auth.models import User

CATEGORY=(
    ('Electronics','Electronics'),
    ('Food','Food'),
    ('Stationary','Stationary')
)

class product(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    quantity=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural='our products'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'