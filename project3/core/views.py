from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
import requests
from django.conf import settings
from .models import Movie
from .forms import MovieForm

# fake data for testing if UI works
MOCK_RECORDS = [
    {'pk': 1, 'id': 1, 'name': 'Sample Movie A', 'date': '2026-01-15', 'source': 'csv', 'numeric_value': 8.5},
    {'pk': 2, 'id': 2, 'name': 'Sample Movie B', 'date': '2026-02-10', 'source': 'api', 'numeric_value': 7.2},
    {'pk': 3, 'id': 3, 'name': 'Sample Movie C', 'date': '2026-03-05', 'source': 'manual', 'numeric_value': 9.1},
]

def home(request):
    return render(request, 'core/home.html')

def record_list(request):
    return render(request, 'core/list.html', {'records': MOCK_RECORDS, 'is_paginated': False})

def record_detail(request, pk):
    record = next((r for r in MOCK_RECORDS if r['pk'] == pk), MOCK_RECORDS[0])
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
    summary_stats = {
        'Total Records': 3,
        'Average Rating': 6.7,
        'Max Rating': 6.7,
        'Min Rating': 6.7
    }
    return render(request, 'core/analytics.html', {
        'summary_stats': summary_stats,
        'chart_json': '{}'
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