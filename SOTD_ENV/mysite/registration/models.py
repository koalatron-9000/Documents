from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key= True)
    first_name = models.CharField(max_length=100, blank= True)
    last_name = models.CharField(max_length=100, blank= True)
    user_name = models.CharField(max_length=100, blank= True)
    occupation = models.CharField(max_length=100, blank= True)
   # profile = imagefield?
    def __str__(self):
        return self.user_name
