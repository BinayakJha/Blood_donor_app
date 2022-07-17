from pyexpat import model
from django.db import models

# Create your models here.

class Blood_form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    blood_group = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    report = models.FileField(upload_to='media', blank = False, null = False)
    reason = models.CharField(max_length=50, blank=True, null=True, default=None)
    #  <!-- time in format of July 17, 2022 -->

    time = models.DateTimeField(auto_now_add=True, null=True)

    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    


