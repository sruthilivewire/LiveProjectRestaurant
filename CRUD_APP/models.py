from django.db import models

# Create your models here.

# Table for Food Items - MAIN_COURSE

class MAIN_COURSE(models.Model):

    item_code = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    item_name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.CharField(max_length=30)
    category = models.CharField(max_length=30)





