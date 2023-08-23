from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView
from .models import Player, Tag
from django.urls import reverse

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
    fields = ["user_name", "assigned_tag_id"]
    template_name = "game/activateoperative.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unassigned_tags'] = Tag.objects.filter(assigned=False)
        return context

    def get_success_url(self):
        return reverse("reserves")