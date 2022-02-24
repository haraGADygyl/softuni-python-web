from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)
