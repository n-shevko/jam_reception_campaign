# Generated by Django 2.2.4 on 2019-08-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birthday', models.DateField()),
                ('citizenship', models.CharField(max_length=50)),
                ('passport_num', models.CharField(max_length=50)),
                ('personal_id', models.CharField(max_length=50)),
                ('passport_exp_date', models.DateField()),
                ('photo_link', models.ImageField(upload_to='')),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField()),
            ],
        ),
    ]