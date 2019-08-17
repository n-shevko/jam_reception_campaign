from django.db import models


class Applicants(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

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
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=FEMALE,
    )


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
    spec_name = models.CharField(max_length=50)
    spec_desc = models.CharField(max_length=250)
    colledge_id = models.ForeignKey(Colleges, on_delete=models.SET_NULL, null=True)
    disable_flag = models.CharField(max_length=1)
    creation_date = models.DateField(auto_now=True)
    last_update_date = models.DateField()


class Applications(models.Model):
    spec = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(Applicants, on_delete=models.SET_NULL, null=True)
    free_education_flag = models.CharField(max_length=1)
    paid_education_flag = models.CharField(max_length=1)
    full_time_education = models.CharField(max_length=1)
    part_time_education = models.CharField(max_length=1)
    after_9_years = models.CharField(max_length=1)
    after_11_years = models.CharField(max_length=1)
    certificate_avg = models.FloatField()
    test_mark_1 = models.IntegerField()
    test_subject_1 = models.CharField(max_length=50)
    test_mark_2 = models.IntegerField()
    test_subject_2 = models.CharField(max_length=50)
    admitted_flag = models.CharField(max_length=50)

    privilege_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)
    last_update_date = models.DateField()