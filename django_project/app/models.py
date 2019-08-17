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