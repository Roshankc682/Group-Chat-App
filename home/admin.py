from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MessageData)
admin.site.register(UserData)
