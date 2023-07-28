from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from scripts.static.scripts import relay_test, net_check

# Create your views here.
class ScriptsPageView(TemplateView):
    template_name = "scripts/scripts.html"

def switch_on(request):
    relay_test.relay_switch(1) 
    return HttpResponseRedirect(reverse('scripts'))

def switch_off(request):
    relay_test.relay_switch(0) 
    return HttpResponseRedirect(reverse('scripts'))

def netcheck(request):
    net_check.netcheck()
    return HttpResponseRedirect(reverse('scripts'))