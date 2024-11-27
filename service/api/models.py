from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):

    created_update=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=False)

    is_active=models.BooleanField(default=True)

class Customer(BaseModel):

    name=models.CharField(max_length=200)

    phone=models.CharField(max_length=12)

    email=models.CharField(max_length=200)

    vehicle_no=models.CharField(max_length=200)

    running_km=models.PositiveIntegerField()

    total_amount=models.PositiveIntegerField()

    service_advisor=models.ForeignKey(User,on_delete=models.CASCADE)

    status_type=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=status_type,default="in-progress")

class JobCard(BaseModel):

    title=models.CharField(max_length=100)

    description=models.CharField(max_length=100)

    amount=models.PositiveIntegerField()

    customer_object=models.ForeignKey(Customer,on_delete=models.CASCADE)


