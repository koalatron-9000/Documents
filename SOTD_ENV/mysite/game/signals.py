from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Player, Tag, Box
from datetime import datetime

aware_datetime = timezone.now()

#@receiver(m2m_changed, sender=Player.player_boxes_collected.through)
#def game_started(sender, instance, action, **kwargs):
#    if action == 'post_add':
#        if instance.player_boxes_collected.filter(box_number=0).exists() and not instance.game_start_time:
#            instance.game_start_time = aware_datetime
#            instance.save()

@receiver(post_save, sender=Player)
def update_assigned_tag(sender, instance, **kwargs):
    if instance.assigned_tag_id:
        tag = instance.assigned_tag_id
        if not tag.assigned:  # Check if the tag is not already assigned
            tag.assigned = True
            tag.save()
            

@receiver(post_save, sender=Player)
def update_unassigned_tag(sender, instance, **kwargs):
    if instance.assigned_tag_id:
        tag = instance.assigned_tag_id
        if tag.assigned:  # Check if the tag is not already assigned
            tag.assigned = False
            tag.save()

@receiver(m2m_changed, sender=Player.player_boxes_collected.through)
def box_updates(sender, instance, action, **kwargs):
    #print(aware_datetime)
    if action == 'post_add':
        #game completion logic
        boxes_needed = Box.objects.all()  # Retrieve all boxes
        if set(instance.player_boxes_collected.all()) == set(boxes_needed):
            print("passed comparison")
            tag = instance.assigned_tag_id
            #if tag and tag.assigned:
            instance.game_completed = True
            instance.game_completion_time = aware_datetime
            print(aware_datetime)
            instance.save()
        #start time logic
        elif instance.player_boxes_collected.filter(box_number=0).exists() and not instance.game_start_time:
            instance.game_start_time = aware_datetime
            instance.save()