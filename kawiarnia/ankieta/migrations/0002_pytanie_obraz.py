# Generated by Django 4.0.2 on 2022-02-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytanie',
            name='obraz',
            field=models.CharField(default='brak.jpg', max_length=300),
        ),
    ]
