from django.contrib import admin
from accounts.models import UserProfile

#how to add columns in admin page, from tutorial 38
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website', 'phone')

    def user_info(self, obj):
        return obj.description
    #user_info.short_description = 'INFO'
    #^ is if i wanted to change USER INFO column header
    # name to INFO in admin page

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        #queryset = queryset.order_by('user')
        return queryset

    #^extremely useful. replace 'user' to choose how to sort
    #user profiles in admin page!!! do -user to do inverse order

admin.site.register(UserProfile, UserProfileAdmin)
