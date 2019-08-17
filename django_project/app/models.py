from django.db import models


class Applicants(models.Model):
    applicant_id = models.IntegerField(db_column='Applicant_ID', primary_key=True)
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)
    middle_name = models.CharField(db_column='Middle_Name', max_length=50, blank=True, null=True)
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)
    date_of_birth = models.DateField(db_column='Date_of_Birth', blank=True, null=True)
    citizenship = models.CharField(db_column='Citizenship', max_length=50, blank=True, null=True)
    passport_num = models.CharField(db_column='Passport_Num', max_length=50, blank=True, null=True)
    personal_id = models.CharField(db_column='Personal_ID', max_length=50, blank=True, null=True)
    passport_exp_date = models.DateField(db_column='Passport_exp_date', blank=True, null=True)
    photo_link = models.CharField(db_column='Photo_link', max_length=240, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Applicants'


class Applications(models.Model):
    application_id = models.IntegerField(primary_key=True)
    spec = models.ForeignKey('Specialties', models.DO_NOTHING, blank=True, null=True)
    applicant = models.ForeignKey(Applicants, models.DO_NOTHING, blank=True, null=True)
    free_education_flag = models.CharField(db_column='Free_education_flag', max_length=1, blank=True, null=True)
    paid_education_flag = models.CharField(db_column='Paid_education_flag', max_length=1, blank=True, null=True)
    full_time_education_flag = models.CharField(db_column='Full_time_education_flag', max_length=1, blank=True,
                                                null=True)
    part_time_education_flag = models.CharField(db_column='Part_time_education_flag', max_length=1, blank=True,
                                                null=True)
    after_9_years_flag = models.CharField(max_length=1, blank=True, null=True)
    after_11_years_flag = models.CharField(max_length=1, blank=True, null=True)
    certificate_avg = models.IntegerField(db_column='Certificate_Avg', blank=True, null=True)
    number_1_test_mark = models.IntegerField(db_column='1_Test_Mark', blank=True, null=True)
    number_1_test_subject_id = models.IntegerField(db_column='1_Test_Subject_id', blank=True, null=True)
    number_2_test_mark = models.IntegerField(db_column='2_Test_Mark', blank=True, null=True)
    number_2_test_subject_id = models.IntegerField(db_column='2_Test_Subject_id', blank=True, null=True)
    admitted_flag = models.CharField(db_column='Admitted_Flag', max_length=1, blank=True, null=True)
    privilege = models.ForeignKey('Privileges', models.DO_NOTHING, db_column='Privilege_id', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Applications'


class CertificateMarks(models.Model):
    certificate = models.ForeignKey('Certificates', models.DO_NOTHING, db_column='Certificate_id', blank=True,
                                    null=True)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Subject_id', blank=True, null=True)
    mark = models.IntegerField(db_column='Mark', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Certificate_Marks'


class Certificates(models.Model):
    certificate_id = models.IntegerField(db_column='Certificate_id', primary_key=True)
    certificate_type = models.CharField(db_column='Certificate_type', max_length=50, blank=True, null=True)
    certificate_date = models.DateField(db_column='Certificate_date', blank=True, null=True)
    certificate_number = models.CharField(db_column='Certificate_number', max_length=50, blank=True, null=True)
    applicant = models.ForeignKey(Applicants, models.DO_NOTHING, db_column='Applicant_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Certificates'


class Colleges(models.Model):
    college_id = models.IntegerField(db_column='College_id', primary_key=True)
    college_name = models.CharField(db_column='College_name', max_length=50, blank=True, null=True)
    college_type = models.CharField(db_column='College_type', max_length=50, blank=True, null=True)
    college_desc = models.CharField(db_column='College_desc', max_length=150, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    def __str__(self):
        return ''.join([word[0] for word in self.college_name.split()]) if self.college_name else ''

    class Meta:
        managed = False
        db_table = 'Colleges'


class ExamTypes(models.Model):
    exam_type_id = models.IntegerField(db_column='Exam_type_id', primary_key=True)
    exam_type_name = models.CharField(db_column='Exam_Type_Name', max_length=50, blank=True, null=True)
    exam_type_desc = models.CharField(db_column='Exam_Type_Desc', max_length=240, blank=True, null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Exam_Types'


class Periods(models.Model):
    period_id = models.IntegerField(db_column='Period_ID', primary_key=True)
    college = models.ForeignKey(Colleges, models.DO_NOTHING, db_column='College_ID', blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    period_type = models.CharField(db_column='Period_type', max_length=50, blank=True, null=True)
    number_9_years_free_education_start_date = models.DateField(db_column='9_years_Free_education_start_date',
                                                                blank=True, null=True)
    number_9_years_free_education_end_date = models.DateField(db_column='9_years_Free_education_end_date', blank=True,
                                                              null=True)
    number_9_years_paid_education_start_date = models.DateField(db_column='9_years_Paid_education_start_date',
                                                                blank=True, null=True)
    number_9_years_paid_education_end_date = models.DateField(db_column='9_years_Paid_education_end_date', blank=True,
                                                              null=True)
    number_11_years_free_education_start_date = models.DateField(db_column='11_years_Free_education_start_date',
                                                                 blank=True, null=True)
    number_11_years_free_education_end_date = models.DateField(db_column='11_years_Free_education_end_date', blank=True,
                                                               null=True)
    number_11_years_paid_education_start_date = models.DateField(db_column='11_years_Paid_education_start_date',
                                                                 blank=True, null=True)
    number_11_years_paid_education_end_date = models.DateField(db_column='11_years_Paid_education_end_date', blank=True,
                                                               null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Periods'


class Privileges(models.Model):
    privilege_id = models.IntegerField(db_column='Privilege_id', primary_key=True)
    privilege_name = models.CharField(db_column='Privilege_name', max_length=50, blank=True, null=True)
    privilege_desc = models.CharField(db_column='Privilege_desc', max_length=240, blank=True, null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Privileges'


class Specialties(models.Model):
    spec_id = models.IntegerField(db_column='Spec_id', primary_key=True)
    spec_name = models.CharField(db_column='Spec_name', max_length=50, blank=True, null=True)
    spec_desc = models.CharField(db_column='Spec_desc', max_length=255, blank=True, null=True)
    colledge = models.ForeignKey(Colleges, models.DO_NOTHING, db_column='Colledge_id', blank=True, null=True)
    disable_flag = models.CharField(db_column='Disable_flag', max_length=1, blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Specialties'


class Statistics(models.Model):
    stat_id = models.IntegerField(db_column='Stat_id', primary_key=True)
    spec = models.ForeignKey(Specialties, models.DO_NOTHING, db_column='Spec_id', blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    free_education_plan = models.IntegerField(db_column='Free_education_plan', blank=True, null=True)
    free_education_passing_score = models.IntegerField(db_column='Free_education_passing_score', blank=True, null=True)
    free_education_app_amt = models.IntegerField(db_column='Free_education_app_amt', blank=True, null=True)
    paid_education_plan = models.IntegerField(db_column='Paid_education_plan', blank=True, null=True)
    paid_education_passing_score = models.IntegerField(db_column='Paid_education_passing_score', blank=True, null=True)
    paid_education_app_amt = models.IntegerField(db_column='Paid_education_app_amt', blank=True, null=True)
    full_time_education_plan = models.IntegerField(db_column='Full_time_education_plan', blank=True, null=True)
    full_time_education_passing_score = models.IntegerField(db_column='Full_time_education_passing_score', blank=True,
                                                            null=True)
    full_time_education_app_amt = models.IntegerField(db_column='Full_time_education_app_amt', blank=True, null=True)
    part_time_education_plan = models.IntegerField(db_column='Part_time_education_plan', blank=True, null=True)
    part_time_education_passing_score = models.IntegerField(db_column='Part_time_education_passing score', blank=True,
                                                            null=True)
    part_time_education_app_amt = models.IntegerField(db_column='Part_time_education_app_amt', blank=True, null=True)
    number_9_year_education_plan = models.IntegerField(db_column='9_year_education_plan', blank=True, null=True)
    number_9_year_education_passing_score = models.IntegerField(db_column='9_year_education_passing_score', blank=True,
                                                                null=True)
    number_9_year_education_app_amt = models.IntegerField(db_column='9_year_education_app_amt', blank=True, null=True)
    number_11_year_education_plan = models.IntegerField(db_column='11_year_education_plan', blank=True, null=True)
    number_11_year_education_passing_score = models.IntegerField(db_column='11_year_education_passing_score',
                                                                 blank=True, null=True)
    number_11_year_education_app_amt = models.IntegerField(db_column='11_year_education_app_amt', blank=True, null=True)
    exam_type = models.ForeignKey(ExamTypes, models.DO_NOTHING, db_column='Exam_type_id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Statistics'


class SubjectPriority(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)
    spec = models.ForeignKey(Specialties, models.DO_NOTHING, db_column='Spec_id', blank=True, null=True)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='Subject_id', blank=True, null=True)
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)
    creation_date = models.DateField(db_column='Creation_date', blank=True, null=True)
    last_update_date = models.DateField(db_column='Last_update_date', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Subject_Priority'


class Subjects(models.Model):
    subject_id = models.IntegerField(db_column='Subject_ID', primary_key=True)
    subject_name = models.CharField(db_column='Subject_name', max_length=50, blank=True, null=True)
    subject_type = models.CharField(db_column='Subject_type', max_length=50, blank=True, null=True)
    subject_desc = models.CharField(db_column='Subject_desc', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Subjects'
