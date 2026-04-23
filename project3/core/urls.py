from django.contrib import admin
from django.urls import path
from . import views
from .views import movie_search

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    # path("", include("core.urls")),
    path('records/', views.record_list, name='record-list'),
    path('records/<int:pk>/', views.record_detail, name='record-detail'),
    path('records/add/', views.record_add, name='record-add'),
    path('records/<int:pk>/edit/', views.record_edit, name='record-edit'),
    path('records/<int:pk>/delete/', views.record_delete, name='record-delete'),
    path('analytics/', views.analytics, name='analytics'),
    path("movies/search/", movie_search, name="movie-search"),
    path("movies/", views.movie_list, name="movie-list"),
    path("movies/add/", views.movie_create, name="movie-create"),
    path("movies/<int:pk>/", views.movie_detail, name="movie-detail"),
    path("movies/<int:pk>/edit/", views.movie_update, name="movie-update"),
    path("movies/<int:pk>/delete/", views.movie_delete, name="movie-delete"),
    path("fetch/", views.fetch_data_view, name="fetch-data"),
]
