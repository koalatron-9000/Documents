from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home/index.html"

