from django.db import models


# Create your models here.

class Admin(models.Model):
    username = models.CharField(default='', max_length=50, verbose_name="username")
    realname = models.CharField(default='', max_length=50, verbose_name="realname")
    password = models.CharField(default='', max_length=32, verbose_name="password")
    gender = models.SmallIntegerField(default=1, verbose_name="gender")  # 1 male，2 female
    status = models.SmallIntegerField(default=1, verbose_name="status")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="addtime")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="updatetime")
    email = models.EmailField(default='', verbose_name="email")

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Doctor(models.Model):
    username = models.CharField(default='', max_length=100, verbose_name="username")
    realname = models.CharField(default='', max_length=50, verbose_name="realname")
    password = models.CharField(default='', max_length=32, verbose_name="password")
    telephone = models.CharField(default='', max_length=50, verbose_name="telephone")
    address = models.CharField(default='', max_length=255, verbose_name="address")
    gender = models.SmallIntegerField(default=1, verbose_name="gender")  # 1 male，2 female
    avatar = models.CharField(default='', max_length=255, verbose_name="avatar")
    status = models.SmallIntegerField(default=1, verbose_name="status")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="addtime")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="updatetime")
    email = models.EmailField(default='', verbose_name="email")

    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Appointment(models.Model):
    doctor_id = models.IntegerField(default=0, verbose_name="doctor_id")
    user_id = models.IntegerField(default=0, verbose_name=" user_id")
    status = models.IntegerField(default=1, verbose_name="status")
    app_date = models.CharField(max_length=255, default='', verbose_name="app_date")
    start_time = models.CharField(max_length=255, default='', verbose_name="start_time")
    symptoms = models.CharField(default='', max_length=255, verbose_name="symptoms")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="addtime")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="updatetime")

    class Meta:
        verbose_name = 'appointment'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.status


class User(models.Model):

    username = models.CharField(default='', max_length=50, verbose_name="username")
    password = models.CharField(default='', max_length=32, verbose_name="password")
    gender = models.SmallIntegerField(default=1, verbose_name="gender")  # 1 male，2 female
    avatar = models.CharField(default='', max_length=255, verbose_name="avatar")
    address = models.CharField(default='', max_length=255, verbose_name="address")
    status = models.SmallIntegerField(default=1, verbose_name="status")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="addtime")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="updatetime")
    email = models.EmailField(default='', verbose_name="email")
    telephone = models.CharField(default='', max_length=20, verbose_name="telephone")
    # add realname in user field
    realname = models.CharField(default='', max_length=50, verbose_name="realname")

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Reports(models.Model):

    doctor_id = models.IntegerField(default=0, verbose_name="doctor_id")
    user_id = models.IntegerField(default=0, verbose_name="user_id")
    appointment_id = models.IntegerField(default=0, verbose_name="appointment_id")
    status = models.SmallIntegerField(default=1, verbose_name="status")
    symptoms = models.CharField(max_length=255, default='', verbose_name="symptoms")
    results = models.CharField(max_length=255, default='', verbose_name="results")
    treatment = models.CharField(max_length=255, default='', verbose_name="treatment")
    desc = models.CharField(max_length=255, default='', verbose_name="desc")
    addtime = models.FloatField(max_length=30, default=0.0, verbose_name="addtime")
    updatetime = models.FloatField(max_length=30, default=0.0, verbose_name="updatetime")

    class Meta:
        verbose_name = 'report'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.status
