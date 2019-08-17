# Generated by Django 2.2.4 on 2019-08-17 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_specialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=50)),
                ('college_desc', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('disable_flag', models.CharField(max_length=1)),
                ('creation_date', models.DateField(auto_now=True)),
                ('last_update_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='specialty',
            name='colledge_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Colleges'),
        ),
    ]
