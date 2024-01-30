from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm, EmailForm
from .models import Profile

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super().get_form()
        # Modifying the form
        form.fields['username'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Username'})
        form.fields['email'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Password'})
        form.fields['password2'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'Confirm Password'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # Return user's profile
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

