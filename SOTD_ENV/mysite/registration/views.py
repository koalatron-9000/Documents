from django.views.generic import TemplateView
# Create your views here.
class RegistrationPageView(TemplateView):
    template_name = "registration/reg.html"