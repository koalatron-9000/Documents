from django import forms
from game.models import Player
from .models import User

class UserIdForm(forms.Form):
    user_id = forms.IntegerField(required=False)

class PlayerForm(forms.ModelForm):
    player_user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, empty_label="Select a user (optional)")
    class Meta:
        model = Player
        fields = ['player_name', 'assigned_tag_id']