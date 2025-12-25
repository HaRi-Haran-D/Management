from django.db import models

# Create your models here.
class Record(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode =models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f'{self.first_name}{self.last_name}')
    

#Admin
#1234