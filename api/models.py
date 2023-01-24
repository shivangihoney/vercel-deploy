from django.db import models

# Create your models here.

class company(models.Model):
    com_name = models.CharField(max_length=50)
    email_id = models.EmailField( max_length=254)