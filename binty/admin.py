from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Genre, Director, Cast, Content, User


admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Cast)
admin.site.register(Content)
admin.site.register(User)