# Generated by Django 3.1.4 on 2020-12-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_peliculafavorita'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='favoritos',
            field=models.IntegerField(default=0),
        ),
    ]