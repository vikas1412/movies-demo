from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from movie.models import Director, NewMovie


class MovieForm(forms.ModelForm):
    class Meta:
        model = NewMovie
        fields = ('title', 'prefix', 'director', 'studio', 'image', 'review', 'genre', 'asin')

    def clean(self):
        cleaned_data = super(MovieForm, self).clean()
        title = cleaned_data['title']
        image = cleaned_data['image']

        if len(str(title)) < 5:
            raise ValidationError(_("Please enter a Proper title for the movie."))
        if image is None:
            raise ValidationError(_("Please select a cover image for the movie."))
        return cleaned_data


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ("first_name", 'middle_name', "last_name", 'number', 'dob', 'website', 'gender')

    def clean(self):
        cleaned_data = super(DirectorForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        number = cleaned_data.get('number')

        if len(str(first_name)) < 5:
            raise ValidationError(_("First name cannot be less than 5 characters or empty"))
        if len(str(last_name)) < 5:
            raise ValidationError(_("Last name cannot be less than 5 characters"))
        if len(str(number)) < 5:
            raise ValidationError(_("Invalid number. Please check the number you have entered."))
        return cleaned_data


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=False, help_text="First Name")
    last_name = forms.CharField(max_length=200, required=False, help_text="Last Name")
    email = forms.CharField(max_length=200, required=False, help_text="Enter email")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
