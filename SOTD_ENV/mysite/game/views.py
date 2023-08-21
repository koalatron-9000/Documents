from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from .models import Player, Tag
from django.urls import reverse

# Create your views here.

class WinnerView(TemplateView):
    template_name = "game/winners.html"
    def get_context_data(self, **kwargs):
        context = super(WinnerView, self).get_context_data(**kwargs)
        context["winners_list"] = Player.objects.filter(game_completed=True)
        return context

class ActivePlayerView(TemplateView):
    template_name = "game/activeplayers.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_players"] = Player.objects.filter(game_completed=None).exclude(assigned_tag_id__isnull =True) 
        return context
    
class WaitingPlayerView(TemplateView):
    template_name = "game/waitingplayers.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["waiting_players"] = Player.objects.filter(game_completed=None).exclude(assigned_tag_id__isnull =False) 
        return context


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