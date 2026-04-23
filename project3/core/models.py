from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
	name = models.CharField(max_length=50, unique=True)

	class Meta: 	
		ordering = ['name']

	def __str__(self):
		return self.name

class Track(models.Model):

	POPULARITY_CHOICES = [
		('Low', 'Low'),
		('Medium', 'Medium'),
		('High', 'High'),
	]

	ENERGY_CHOICES = [
		('Low', 'Low'),
		('Medium', 'Medium'),
		('High', 'High'),
	]

	SOURCE_CHOICES = [
		('csv', 'CSV Import'),
		('api', 'API Fetch'),
	]

	track_id = models.CharField(max_length=30, help_text="Spotify tracj ID")
	name = models.CharField(max_length=200)
	artists = models.CharField(max_length=300)
	album_name = models.CharField(max_length=200)

	genre = models.ForeignKey(
		Genre,
		on_delete=models.CASCADE,
		related_name='tracks',
	)

	popularity = models.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(100)],
		help_text="Spotify popularity score (0-100)",
	)
	duration_ms = models.IntegerField(help_text="Track duration in milliseconds")
	explicit = models.BooleanField(default=False)

	danceability = models.FloatField(help_text="0.0 to 1.0")
	energy = models.FloatField(help_text="0.0 to 1.0")
	loudness = models.FloatField(help_text="Decibals, typically -60 to 0")
	liveness = models.FloatField(help_text="0.0 to 1.0")
	valence = models.FloatField(help_text="0.0 to 1.0, musical positiveness")
	temp = models.FloatField(help_text="BPM")

	popularity_level = models.CharField(
		max_length = 10,
		choices=POPULARITY_CHOICES,
		default='Low',
	)
	energy_level = models.CharField(
		max_length=10,
		choices=ENERGY_CHOICES,
		default='Low',
	)
	source = models.CharField(
		max_length=10,
		choices=SOURCE_CHOICES,
		default='csv',
	)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-popularity']
		unique_together = ['track_id', 'genre']

	def __str__(self):
		return f"{self.name} - {self.artists}"

	@property
	def duration_display(self):
		total_seconds = self.duration_ms // 1000
		minutes = total_seconds // 60
		seconds = total_seconds % 60
		return f"{minutes}:{seconds:02d}"

class DataRun(models.Model):
	
	SOURCE_CHOICES = [
		('csv', 'CSV Import'),
		('spi', 'API Fetch'),
	]

	source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
	records_loaded = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	notes = models.TextField(blank=True, default='')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f"{self.get_source_display()} - {self.records_loaded} records ({self.timestamp: %Y-%m-%d %H:%M})"

class Movie(models.Model):

	imdb_id = models.CharField(max_length=20, unique=True)
	title = models.CharField(max_length=300)
	year = models.CharField(max_length=10)
	rated = models.CharField(max_length=20, blank=True, default='')
	genre = models.CharField(max_length=200, blank=True, default='')
	director = models.CharField(max_length=200, blank=True, default='')
	plot = models.TextField(blank=True, default='')
	imdb_rating = models.FloatField(null=True, blank=True)
	poster_url = models.URLField(max_length=500, blank=True, default='')
	source = models.CharField(
		max_length=10,
		choices=[('api', 'API Fetch')],
		default='api',
	)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-imdb_rating']

	def __str__(self):
		return f"{self.title} ({self.year})"
