# Generated by Django 2.2.14 on 2021-10-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0015_auto_20211016_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('history', models.CharField(max_length=30)),
            ],
        ),
    ]
