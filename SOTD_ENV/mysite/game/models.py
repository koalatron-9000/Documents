from django.db import models
from registration.models import User

# Create your models here.
class Box(models.Model):
    box_number = models.IntegerField(primary_key= True)
    location = models.TextField(max_length= 250, blank=True)
    hint = models.TextField(max_length= 500, blank=True)

    def __str__(self):
        return str(self.box_number)
   
class Tag(models.Model):
    tag_id = models.IntegerField(primary_key= True)
    assigned = models.BooleanField(default= False)

    def __str__(self):
        return str(self.tag_id)

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.TextField(max_length= 300)
    player_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    player_boxes_collected = models.ManyToManyField(Box, blank = True)
    assigned_tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name
