# Generated by Django 2.2.14 on 2021-09-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('experience', models.TextField()),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
    ]
