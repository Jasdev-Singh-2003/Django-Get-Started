from django.db import models

# Create your models here.

class userModel(models.Model):
  name = models.CharField(max_length=100)
  contact = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  def __str__(self) -> str:
    return self.name+" - "+str(self.id)
  
class Product(models.Model):
  product_image = models.FileField(upload_to="uploaded_images/")
  description = models.CharField(max_length=200)
  price = models.FloatField()
  discount = models.IntegerField()
  net_price = models.FloatField()
  def __str__(self) -> str:
    return self.description+" - "+str(self.id)
