from django.contrib import admin
from home.models import Post, Friend, Application
from django.db.models.signals import post_save

# Register your models here.
# We see these in admin view under application
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'bedtime', 'major')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Friend)
admin.site.register(Post)
