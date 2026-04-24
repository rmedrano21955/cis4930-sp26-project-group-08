from django.core.management.base import BaseCommand
from core.services.imdb_api import fetch_movies
from core.models import Movie
import requests
import os
from django.conf import settings

class Command(BaseCommand):
    help = "Fetch movies from OMDb API and store in DB"

    def handle(self, *args, **kwargs):

        api_key = "5589e759"
        url = "http://www.omdbapi.com/"

        for page in range(1, 4):
            try:
                response = requests.get(
                    url,
                    params={
                        "apikey": api_key,
                        "s": "batman",
                        "page": page
                    },
                    timeout=10
                )

                response.raise_for_status()
                data = response.json()

                if "Search" not in data:
                    continue

                for item in data["Search"]:

                    Movie.objects.update_or_create(
                        imdb_id=item["imdbID"],
                        defaults={
                            "title": item["Title"],
                            "year": item["Year"],
                        }
                    )

                self.stdout.write(f"Page {page} imported successfully")

            except requests.exceptions.RequestException as e:
                self.stderr.write(str(e))