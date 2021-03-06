# Generated by Django 2.2.14 on 2021-10-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0013_play_poem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='lines',
        ),
        migrations.RemoveField(
            model_name='poem',
            name='stanzas',
        ),
        migrations.RemoveField(
            model_name='poem',
            name='style',
        ),
        migrations.RemoveField(
            model_name='poem',
            name='title',
        ),
        migrations.AddField(
            model_name='poem',
            name='uri',
            field=models.URLField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
