from django.contrib import admin
from .models import People, Games , Genres
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(People)
admin.site.register(Games)
admin.site.register(Genres)
