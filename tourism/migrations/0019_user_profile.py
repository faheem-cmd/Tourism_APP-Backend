# Generated by Django 2.2.14 on 2021-10-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0018_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
