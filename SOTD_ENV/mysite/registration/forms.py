from django import forms
from game.models import Player, Tag

class UserIdForm(forms.Form):
    user_id = forms.IntegerField(max_value=9999999999, required=False)
    

class PlayerForm(forms.ModelForm):
    
    class Meta:
        model = Player
        exclude = ['player_boxes_collected', 'game_completed', 'profile_creation_time', 'game_start_time']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_tag_id'].queryset = Tag.objects.filter(assigned=False)