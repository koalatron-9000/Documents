from django.db import models

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
    user_id = models.IntegerField(blank=True, null = True)
    first_name = models.CharField(max_length=100, blank= True)
    last_name = models.CharField(max_length=100, blank= True)
    user_name = models.CharField(max_length=100, blank= True)
    occupation = models.CharField(max_length=100, blank= True)
    player_boxes_collected = models.ManyToManyField(Box, blank = True)
    assigned_tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    game_completed = models.BooleanField(blank=True, null= True)
    profile_creation_time = models.DateTimeField(auto_now=True)
    game_start_time = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.user_name
