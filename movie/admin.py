from django.contrib import admin

from movie.models import Director, Genre


@admin.register(Genre)
class DirectorInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


@admin.register(Director)
class DirectorInstanceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number', 'website')
