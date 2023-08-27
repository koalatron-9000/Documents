from ninja import NinjaAPI, ModelSchema
from game.models import Player
from typing import List
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class PlayerSchema(ModelSchema):
    class Config:
        model = Player
        #model_exclude = ['player_boxes_collected', 'game_completed', 'profile_creation_time', 'game_start_time']
        model_fields = "__all__"

@api.get('/players', response=List[PlayerSchema])
def get_all_players(request):
    return Player.objects.all()

@api.get('/player/{tag_id}', response=PlayerSchema)
def get_player(request, tag_id: int):
    player = get_object_or_404(Player, assigned_tag_id =tag_id)
    return player

@api.put('/{box_id}/{tag_id}', response=PlayerSchema)
def update_player(request, box_id: int, tag_id: int):
    player = get_object_or_404(Player, assigned_tag_id = tag_id)
    player.player_boxes_collected.add(box_id)
    return player