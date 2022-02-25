from django import forms

from exam_01_10_2020.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }
