from django.contrib import admin
from .models import Man, Action, UserAction
# Register your models here.

admin.site.register(Man)
admin.site.register(Action)
admin.site.register(UserAction)
