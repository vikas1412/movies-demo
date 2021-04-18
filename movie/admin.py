from django.contrib import admin

from movie.models import Director, Genre, Studio, NewMovie


@admin.register(Genre)
class DirectorInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


@admin.register(Director)
class DirectorInstanceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'number', 'website')


@admin.register(Studio)
class StudioInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'website', 'timestamp')


@admin.register(NewMovie)
class NewMovieInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'studio', 'release_date')
