from django.core.management.base import BaseCommand
from core.services.imdb_api import fetch_movies
from core.models import Movie
import requests

class Command(BaseCommand):
    help = "Fetch movies from API"

    def handle(self, *args, **kwargs):
        
        url = "http://www.omdbapi.com/"
        api_key = "5589e759"

        try:
            for page in range(1, 4):
                response = requests.get(
                    url,
                    params={
                        "apikey": api_key,
                        "s": "john wick",
                        "page": page
                    },
                    timeout=10
                )

                response.raise_for_status()
                data = response.json()

                self.stdout.write(f"Page {page} fetched successfully")

        except requests.exceptions.RequestException as e:
            self.stderr.write(str(e))