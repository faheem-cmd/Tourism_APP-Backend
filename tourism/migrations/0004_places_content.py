# Generated by Django 2.2.14 on 2021-09-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='content',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]