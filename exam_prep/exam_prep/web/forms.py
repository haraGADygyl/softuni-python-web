import os

from django import forms

from exam_prep.web.models import Profile, Expense


class CreateProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',
        }


class EditProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',
        }


class DeleteProfileFrom(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseFrom(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')

        labels = {
            'image': 'Link to Image',
        }


class EditExpenseFrom(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')

        labels = {
            'image': 'Link to Image',
        }


class DeleteExpenseFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')

        labels = {
            'image': 'Link to Image',
        }
