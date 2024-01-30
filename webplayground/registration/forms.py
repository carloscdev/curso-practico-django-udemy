from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido", widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        # Validating email
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido", widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        # Validating email
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya existe, prueba con otro.")
        return email