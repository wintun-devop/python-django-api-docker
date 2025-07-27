from pyexpat import model
from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    #set only once at creation
    created_at = models.DateTimeField(auto_now_add=True)
    #updated each time model is saved  
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (
            f"Product(id={self.id}, name='{self.name}', model='{self.model}', "
            f"price={self.price}, quantity={self.quantity}, "
            f"created_at='{self.created_at}', updated_at='{self.updated_at}')"
        )
