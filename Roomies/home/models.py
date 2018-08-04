from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)

class Application(models.Model):
    first_name = models.CharField(max_length=50, default='-')
    last_name = models.CharField(max_length=50, default='-')
    email = models.EmailField(max_length=50, default='-')
    bedtime = models.CharField(max_length=50, default='-')
    graduating_class = models.CharField(max_length=50, default='NA')
    major = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_image')

'''class Message(models.Model):
    current_user = models.ForeignKey(User, related_name='messager', null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='-')
    content = models.CharField(max_length=500, default='-')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def add_message(cls, current_user, new_message):
        mes
'''
