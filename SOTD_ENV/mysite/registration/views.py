from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .forms import UserIdForm, PlayerForm
from game.models import Player, Tag


# Create your views here.
class SuccessView(TemplateView):
    template_name = "registration/success.html" 

class NeoNavView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserIdForm

    def form_valid(self, form):
        user_id = form.cleaned_data['user_id']
        
        # Make the API call to fetch user data based on the user_id
        # Example:
        # response = make_api_call_to_get_user_data(user_id)

        # Assuming the API returns a JSON response containing user data
        
        user_data = {
            #'user_id': '0123456789',
            #'first_name': 'John',
            #'last_name': 'Doe',
            #'user_name': 'johndoe',
            #'occupation': 'Engineer',
            #Add other fields from the API response as needed
        }

        # Pass the user_data to the next view using query parameters
        redirect_url = reverse('register') + f'?user_data={user_data}'
        return redirect(redirect_url)

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('success_url')
    
    def get_initial(self):
        user_data = self.request.GET.get('user_data')
        if user_data:
            user_data_dict = eval(user_data)  # Convert the string to a dictionary
            return user_data_dict
        return {}
