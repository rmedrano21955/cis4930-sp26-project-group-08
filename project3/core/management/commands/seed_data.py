import csv
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Genre, Track, DataRun

class Command(BaseCommand):
	help = 'Load Project 1 Spotify CSV data into the database'

	def handle(self, *args, **options):
		csv_path = os.path.join('data', 'raw', 'sample.csv')

		if not os.path.exists(csv_path):
			self.stderr.write(self.style.ERROR(f'CSV not found at {csv_path}'))
			return

		loaded = 0
		skipped = 0

		with open(csv_path, newline='', encoding='utf-8') as f:
			reader = csv.DictReader(f)

			with transaction.atomic():
				for row in reader:
					try:
						genre, _ = Genre.objects.get_or_create(
							name=row['track_genre'].strip()
						)

						pop = int(row['popularity'])
						if pop >= 60:
							pop_level = 'High'
						elif pop >= 30:
							pop_level = 'Medium'
						else:
							pop_level = 'Low'

						energy = float(row['energy'])
						if energy >= 0.66:
							energy_lvl = 'High'
						elif energy >= 0.33:
							energy_lvl = 'Medium'
						else:
							energy_lvl = 'Low'

						explicit = row['explicit'].strip().lower() == 'true'

						_, created = Track.objects.update_or_create(
							track_id=row['track_id'].strip(),
							genre=genre,
							defaults={
								'name': row['track_name'].strip(),
								'artists': row['artists'].strip(),
								'album_name': row['album_name'].strip(),
								'popularity': pop,
								'duration_ms': int(row['duration_ms']),
								'explicit': explicit,
								'danceability': float(row['danceability']),
								'energy': energy,
								'loudness': float(row['loudness']),
								'liveness': float(row['liveness']),
								'valence': float(row['valence']),
								'tempo': float(row['tempo']),
								'popularity_level': pop_level,
								'energy_level': energy_lvl,
								'source': 'csv',
							},
						)

						if created:
							loaded += 1
						else:
							skipped += 1

					except Exception as e:		
						self.stderr.write(
							self.style.WARNING(f'Skipped row: {e}')
						)
						skipped += 1

		DataRun.objects.create(
			source='csv',
			records_loaded=loaded,
			notes=f'Seeded frm {csv_path}, {loaded} created, {skipped} updated/skipped.',
		)

		self.stdout.write(self.style.SUCCESS(
			f'Done: {loaded} trackes created, {skipped} updated/skipped.'
		))	
