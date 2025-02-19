# Generated by Django 4.2 on 2024-10-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_alter_conference_category'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='reservations',
            field=models.ManyToManyField(through='users.Reservation', to='conferences.conference'),
        ),
    ]
