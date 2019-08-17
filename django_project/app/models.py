from django.db import models


class Applicants(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birthday = models.DateField()
    citizenship = models.CharField(max_length=50)
    passport_num = models.CharField(max_length=50)
    personal_id = models.CharField(max_length=50)
    passport_exp_date = models.DateField()
    photo_link = models.ImageField()
    creation_date = models.DateField(auto_now=True)
    last_update_date = models.DateField()


class Colleges(models.Model):
    college_name = models.CharField(max_length=50)
    college_desc = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    disable_flag = models.CharField(max_length=1)
    creation_date = models.DateField(auto_now=True)
    last_update_date = models.DateField()


class Specialty(models.Model):
    spec_id = models.IntegerField()
    spec_name = models.CharField(max_length=50)
    spec_desc = models.CharField(max_length=250)
    colledge_id = models.ForeignKey(Colleges, on_delete=models.SET_NULL, null=True)
    disable_flag = models.CharField(max_length=1)
    creation_date = models.DateField(auto_now=True)
    last_update_date = models.DateField()
