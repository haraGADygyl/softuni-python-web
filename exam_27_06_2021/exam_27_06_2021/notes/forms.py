from django import forms

from exam_27_06_2021.notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Link to Profile Image',
        }


class CreateNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }


class EditNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }


class DeleteNotesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }
