from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from .forms import UserIdForm, PlayerForm
from game.models import Player, Tag


# Create your views here.
class RegistrationPageView(TemplateView):
    template_name = "registration/reg.html"


class RegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserIdForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unassigned_tags'] = Tag.objects.filter(assigned=False)
        return context

    def form_valid(self, form):
        user_id = form.cleaned_data['user_id']
        
        if user_id is not None:
            # Make the API call to fetch user data based on the user_id
            # Example:
            # response = make_api_call_to_get_user_data(user_id)

            # Assuming the API returns a JSON response containing user data
            user_data = {
                'user_id': '0123456789',
                'first_name': 'John',
                'last_name': 'Doe',
                'user_name': 'johndoe',
                'occupation': 'Engineer',
                # Add other fields from the API response as needed
            }

            # Populate the form with the fetched user data
            form.fields['user_id'].initial = user_data['user_id']
            form.fields['first_name'].initial = user_data['first_name']
            form.fields['last_name'].initial = user_data['last_name']
            form.fields['user_name'].initial = user_data['user_name']
            form.fields['occupation'].initial = user_data['occupation']

            # You can also pass the user_data to the template and render it if needed

            return render(self.request, self.template_name, {'form': form, 'user_data': user_data})
        else:
            # If user_id is None, it means it's a new player registration using PlayerForm
            player_form = PlayerForm(self.request.POST)  # Instantiate PlayerForm with POST data
            if player_form.is_valid():
                user_instance, _ = Player.objects.get_or_create(
                    #user_id = player_form.cleaned_data['user_id'],
                    #first_name = player_form.cleaned_data['first_name'],
                    #last_name = player_form.cleaned_data['last_name'],
                    user_name=player_form.cleaned_data['user_name'],
                    assigned_tag_id=player_form.cleaned_data['assigned_tag_id']
                
                    # Add other fields from the form as needed
                )

                # Set the player_user field to the User instance
                player_form.instance.player_user = user_instance
                player_form.save()  # Save the new player to the database
                return redirect('success_url')  # Replace 'success_url' with the URL you want to redirect to after successful submission
            else:
                return render(self.request, self.template_name, {'form': player_form})