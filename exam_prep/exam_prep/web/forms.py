from django.forms import models

from exam_prep.web.models import Profile


class CreateProfileFrom(models.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class EditProfileFrom(models.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')
