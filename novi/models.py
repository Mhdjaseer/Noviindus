from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media/products')
    category=models.CharField(max_length=30)
    model_Name=models.CharField(max_length=50)
    price=models.IntegerField()
    
    def __str__(self) :
        return self.title
    

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(Item)

    def __str__(self):
        return f" Cart list for {self.user.username}"