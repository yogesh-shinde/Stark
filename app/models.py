from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Adminmodel(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )

    adminid = models.CharField(max_length=36, default=None, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'admin_model'
        verbose_name = "Admin Model"
        verbose_name_plural = "Admin Model"

    def save(self, **kwargs):
        super(Adminmodel, self).save(**kwargs)
        self.adminid = 'AM%04d' % self.pk
        Adminmodel.objects.filter(pk=self.pk).update(adminid=self.adminid)

    def __str__(self):
        return str(self.adminid)

class Usermodel (models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'not specified'),
    )

    userid = models.CharField(max_length=36, default=None, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_model'
        verbose_name = "User Model"
        verbose_name_plural = "User Model"

    def save(self, **kwargs):
        super(Usermodel, self).save(**kwargs)
        self.userid = 'UM%04d' % self.pk
        Usermodel.objects.filter(pk=self.pk).update(userid=self.userid)

    def __str__(self):
        return str(self.userid)


class Movies(models.Model):
    movieid = models.CharField(max_length=36, default=None, null=True, blank=True)
    name = models.CharField(max_length=36, default=None, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', max_length=254)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'movies'
        verbose_name = "Movies"
        verbose_name_plural = "Movies"

    def save(self, **kwargs):
        super(Movies, self).save(**kwargs)
        self.movieid = 'M%04d' % self.pk
        Movies.objects.filter(pk=self.pk).update(movieid=self.movieid)

    def __str__(self):
        return str(self.name)