from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
import requests
from django.conf import settings
from .models import Genre, Track, DataRun, Movie
from .forms import MovieForm
from django.core.management import call_command
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
import json
import pandas as pd

# fake data for testing if UI works
MOCK_RECORDS = [
    {'pk': 1, 'id': 1, 'name': 'Sample Record A', 'date': '2026-01-15', 'source': 'csv', 'numeric_value': 8.5},
    {'pk': 2, 'id': 2, 'name': 'Sample Record B', 'date': '2026-02-10', 'source': 'api', 'numeric_value': 7.2},
    {'pk': 3, 'id': 3, 'name': 'Sample Record C', 'date': '2026-03-05', 'source': 'manual', 'numeric_value': 9.1},
]

def home(request):
    return render(request, 'core/home.html')

def record_list(request):
    tracks = Track.objects.select_related('genre').all()
    paginator = Paginator(tracks, 20)
    page = request.GET.get('page')
    tracks_page = paginator.get_page(page)
    return render(request, 'core/list.html', {'records': tracks_page, 'is_paginated': True})

def record_detail(request, pk):
    record = get_object_or_404(Track, pk=pk)
    return render(request, 'core/detail.html', {'record': record})

def record_add(request):
    return render(request, 'core/form.html', {'form': [], 'record': None})

def record_edit(request, pk):
    record = next((r for r in MOCK_RECORDS if r['pk'] == pk), MOCK_RECORDS[0])
    return render(request, 'core/form.html', {'form': [], 'record': record})

def record_delete(request, pk):
    record = next((r for r in MOCK_RECORDS if r['pk'] == pk), MOCK_RECORDS[0])
    return render(request, 'core/confirm_delete.html', {'record': record})

def analytics(request):
    from .models import Track
    qs = Track.objects.select_related('genre').values(
        'genre__name', 'popularity', 'energy', 'danceability',
        'valence', 'tempo', 'loudness'
    )
    df = pd.DataFrame(list(qs))

    pop_by_genre = df.groupby('genre__name')['popularity'].mean().round(2).sort_values(ascending=False).head(10)
    bar_chart = {
        'labels': pop_by_genre.index.tolist(),
        'values': pop_by_genre.values.tolist(),
    }

    energy_dist = df['energy'].apply(
        lambda x: 'High' if x >= 0.7 else ('Medium' if x >= 0.4 else 'Low')
    ).value_counts()
    pie_chart = {
        'labels': energy_dist.index.tolist(),
        'values': energy_dist.values.tolist(),
    }

    summary = {
        'Total Tracks': len(df),
        'Avg Popularity': round(df['popularity'].mean(), 2),
        'Max Popularity': int(df['popularity'].max()),
        'Min Popularity': int(df['popularity'].min()),
        'Avg Energy': round(df['energy'].mean(), 3),
        'Avg Danceability': round(df['danceability'].mean(), 3),
        'Avg Tempo (BPM)': round(df['tempo'].mean(), 2),
    }

    return render(request, 'core/analytics.html', {
        'bar_chart_json': json.dumps(bar_chart),
        'pie_chart_json': json.dumps(pie_chart),
        'summary_stats': summary,
    })

def movie_search(request):
    query = request.GET.get("q", "john wick")

    url = "http://www.omdbapi.com/"

    params = {
        "apikey": settings.API_KEY,
        "s": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    movies = data.get("Search", [])

    return render(request, "movies/search.html", {
        "movies": movies,
        "query": query
    })

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/list.html", {"movies": movies})

def movie_create(request):
    print("TEMPLATE: movies/form.html")
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie-list")
    else:
        form = MovieForm()
    
    return render(request, "movies/form.html", {"form": form})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect("movie-list")
    
    return render(request, "movies/form.html", {"form": form})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movies/detail.html", {"movie": movie})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        movie.delete()
        return redirect("movie-list")
    
    return render(request, "movies/confirm_delete.html", {"movie": movie})

@staff_member_required
@require_POST
def fetch_data_view(request):
    call_command("fetch_data")  
    return redirect("movie-list")