from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

class UserProfileManager(models.Manager):
    def get_queryset(self):
        #return super(UserProfileManager, self).get_queryset().filter(city='Chicago')
        return super(UserProfileManager, self).get_queryset().filter(user='test')

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to=user_directory_path, default='media/profile_image/user_profile_pic_default.jpg')
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
