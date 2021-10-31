# Generated by Django 2.2.14 on 2021-10-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0007_auto_20211007_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='imageURL',
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.URLField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]
