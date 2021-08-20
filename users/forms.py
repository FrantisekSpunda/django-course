from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        self.fields['first_name'].widget.attrs.update({'id': 'formInput#text', 'placeholder':'e.g. Dennis Ivanov'})
        self.fields['email'].widget.attrs.update({'id': 'formInput#email', 'placeholder':'e.g. user@domain.com'})
        self.fields['username'].widget.attrs.update({'id': 'formInput#text', 'placeholder':'e.g. dennis.ivanov'})
        self.fields['password1'].widget.attrs.update({'id': 'formInput#passowrd', 'placeholder':'••••••••'})
        self.fields['password2'].widget.attrs.update({'id': 'formInput#confirm-passowrd', 'placeholder':'••••••••'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 'short_intro', 'profile_image', 'social_github', 'social_linkedin', 'social_twitter', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})