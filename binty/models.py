from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=200, unique=True)
    portrait = models.ImageField(upload_to='portrait/', null=True)
    history = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class User(AbstractUser):

    icon = models.ImageField(upload_to='icon/', null=True, blank=True)
    good = models.ManyToManyField(Cast, blank=True, verbose_name='イイね', default=[1])

    def __str__(self):
        return super().username


class Content(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    country = models.CharField(max_length=100)
    release_date = models.DateTimeField(null=True)
    genre = models.ForeignKey(Genre, verbose_name='ジャンル', on_delete=models.CASCADE, null=True)
    director = models.ForeignKey(Director, verbose_name='監督', on_delete=models.PROTECT, null=True)
    cast = models.ManyToManyField(Cast, blank=True, verbose_name='キャスト', null=True)
    awards = models.CharField(max_length=200, null=True)
    goods = models.ManyToManyField(User, null=True, verbose_name='イイね！')
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title



