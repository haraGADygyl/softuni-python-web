from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    image_url = models.URLField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    content = models.TextField()

    class Meta:
        ordering = ('title',)
