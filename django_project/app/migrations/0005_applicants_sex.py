# Generated by Django 2.2.4 on 2019-08-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190817_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
    ]
