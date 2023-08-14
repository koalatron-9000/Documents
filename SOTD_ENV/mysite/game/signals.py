from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Player, Tag, Box

@receiver(post_save, sender=Player)
def update_assigned_tag(sender, instance, **kwargs):
    if instance.assigned_tag_id:
        tag = instance.assigned_tag_id
        if not tag.assigned:  # Check if the tag is not already assigned
            tag.assigned = True
            tag.save()

@receiver(m2m_changed, sender=Player.player_boxes_collected.through)
def check_boxes_collected(sender, instance, action, **kwargs):
    if action == 'post_add':
        boxes_needed = Box.objects.all()  # Retrieve all boxes
        if set(instance.player_boxes_collected.all()) == set(boxes_needed):
            tag = instance.assigned_tag_id
            if tag and tag.assigned:
                tag.assigned = False
                tag.save()
                instance.assigned_tag_id = None
                instance.game_completed = True
                instance.save()