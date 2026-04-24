from django.core.management.base import BaseCommand
from core.services.imdb_api import fetch_movies
from core.models import Movie
import requests
import os
from django.conf import settings

class Command(BaseCommand):
    help = "Fetch movies from API"

    def handle(self, *args, **kwargs):
        
        api_key = settings.API_KEY

        if not api_key:
            self.stderr.write("Missing API_KEY in environment")
            return

        url = "http://www.omdbapi.com/"

        try:
            response = requests.get(
                url,
                params={
                    "apikey": api_key,
                    "s": "batman"
                },
                timeout=10
            )

            response.raise_for_status()
            data = response.json()

            self.stdout.write(str(data))

        except requests.exceptions.RequestException as e:
            self.stderr.write(str(e))