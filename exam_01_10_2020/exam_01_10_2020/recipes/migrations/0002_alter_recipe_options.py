# Generated by Django 4.0.2 on 2022-02-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('title',)},
        ),
    ]