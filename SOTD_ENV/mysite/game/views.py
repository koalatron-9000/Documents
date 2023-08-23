from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView
from .models import Player
from django.urls import reverse_lazy
from registration.forms import PlayerForm

# Create your views here.

class GHomeView(TemplateView):
    template_name = 'game/gamehome.html'

class WinnerView(ListView):
    template_name = "game/winners.html"
    queryset = Player.objects.filter(game_completed=True)
    context_object_name = 'winners'

class ActivePlayerView(ListView):
    template_name = "game/activeplayers.html"
    queryset = Player.objects.filter(game_completed=None).exclude(assigned_tag_id__isnull =True)
    context_object_name = 'active_agents'
    
class WaitingPlayerView(ListView):
    template_name = "game/waitingplayers.html"
    queryset = Player.objects.filter(game_completed=None).exclude(assigned_tag_id__isnull =False) 
    context_object_name = 'reserve_agents'

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = "game/activateoperative.html"
    form_class = PlayerForm
    success_url = reverse_lazy('reserves')