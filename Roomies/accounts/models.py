from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

class UserProfileManager(models.Manager):
    def get_queryset(self):
        #return super(UserProfileManager, self).get_queryset().filter(city='Chicago')
        return super(UserProfileManager, self).get_queryset().filter(user='test')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Chicago = UserProfileManager()
    #^ for model manager, in django shell, run
    #from accounts.models import UserProfile, then
    # UserProfile.Chicago.all()
    # to get all user accounts with city equaling Chicago
    #in Tutorial 40

    def __str__(self):
        return self.user.username




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
