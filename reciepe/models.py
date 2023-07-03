from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reciepe_Details(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=100,)
    incredients =models.CharField(max_length=500,)
    procedure=models.CharField(max_length=800)
    food_img=models.ImageField(null=True)
    
    def __str__(self) -> str:
        return self.food_name