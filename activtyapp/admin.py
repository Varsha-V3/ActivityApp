from django.contrib import admin
# from django.contrib.auth.models import User
# Register your models here.
from .models import Status,Members,ActivityPeriod
# ,CustomUser
admin.site.register(Status)
admin.site.register(Members)
admin.site.register(ActivityPeriod)
# admin.site.register(User)