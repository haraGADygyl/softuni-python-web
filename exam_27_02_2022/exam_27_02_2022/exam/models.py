from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
def validate_username(value):
    if not value.isalnum() or not '_':
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username,
        )
    )

    email = models.EmailField(

    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        )
    )


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R&B Music', 'R&B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other'),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(

    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )
    )

    class Meta:
        ordering = (
            'album_name',
        )

