# Generated by Django 4.2 on 2023-08-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
