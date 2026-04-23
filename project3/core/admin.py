from django.contrib import admin
from .models import Genre, Track, DataRun, Movie

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
	list_display = ('name', 'artists', 'genre', 'popularity', 'energy', 'tempo', 'source')
	search_fields = ('name', 'artists', 'album_name')
	list_filter = ('genre', 'source', 'explicit', 'popularity_level', 'energy_level')
	list_per_page = 25

@admin.register(DataRun)
class DataRunAdmin(admin.ModelAdmin):
	list_display = ('source', 'records_loaded', 'timestamp')
	list_filter = ['source']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'year', 'director', 'imdb_rating')
	search_fields = ('title', 'director')
	list_filter = ('rated', 'year')
	
