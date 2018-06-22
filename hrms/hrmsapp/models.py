from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class auth_user_extended(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, to_field='id')
    is_role = models.CharField(max_length=100)
    is_designation = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_pics', blank=True)
    mobile_no = models.CharField(max_length=100)
    add_skill = models.CharField(max_length=100, blank=True, null=True)


class payroll(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    basic_sal = models.IntegerField(blank=True, null=True)
    hra = models.IntegerField(blank=True)
    conveyance = models.IntegerField(blank=True)
    pf_employer = models.IntegerField(blank=True)
    performance_allowance = models.IntegerField(blank=True)
    arrears = models.IntegerField(blank=True)
    others = models.IntegerField(blank=True)
    incentives = models.IntegerField(blank=True)
    total_earning = models.IntegerField(blank=True)
    pf_employee = models.IntegerField(blank=True)
    prof_tax = models.IntegerField(blank=True)
    advance = models.IntegerField(blank=True)
    IT_ded = models.IntegerField(blank=True)
    total_ded = models.IntegerField(blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)

    def __str__(self):
        return self.basic_sal

class basic_info(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    temp_addrs = models.CharField(max_length=100, blank=True, null=True)
    temp_state = models.CharField(max_length=100, blank=True, null=True)
    temp_city = models.CharField(max_length=100, blank=True, null=True)
    temp_pincode = models.CharField(max_length=100, blank=True, null=True)
    permanent_addrs = models.CharField(max_length=100, blank=True, null=True)
    permanent_state = models.CharField(max_length=100, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_pincode = models.CharField(max_length=100, blank=True, null=True)
    documents_submitted = models.CharField(max_length=100, blank=True, null=True)
    emerg_name = models.CharField(max_length=100, blank=True, null=True)
    emerg_contact = models.CharField(max_length=100, blank=True, null=True)
    emerg_relation = models.CharField(max_length=100, blank=True, null=True)
    emerg_occupation = models.CharField(max_length=100, blank=True, null=True)

class personnel_info(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    gender = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    pan = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField()
    doj = models.DateField()
    contact = models.IntegerField(blank=True, null=True)
    altr_email = models.EmailField(max_length=100, blank=True, null=True)
    blood_grp = models.CharField(max_length=100, blank=True, null=True)

class experience_info(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    organization = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    period_from = models.DateField()
    period_to = models.DateField()
    leaving_reason = models.CharField(max_length=100, blank=True, null=True)

class educational_info(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    level = models.CharField(max_length=100, blank=True, null=True)
    passing_year = models.CharField(max_length=100, blank=True, null=True)
    marks = models.IntegerField(blank=True)
    board = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)

class holidays(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    holiday_date = models.CharField(max_length=100, blank=True, null=True)
    holiday_day = models.CharField(max_length=100, blank=True,null=True)

class attendance(models.Model):
    emp = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username')
    login_time = models.DateTimeField()
    logout_time = models.CharField(max_length=100, blank=True, null=True)

