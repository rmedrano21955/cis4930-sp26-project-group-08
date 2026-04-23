from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.record_list, name='record-list'),
    path('records/<int:pk>/', views.record_detail, name='record-detail'),
    path('records/add/', views.record_add, name='record-add'),
    path('records/<int:pk>/edit/', views.record_edit, name='record-edit'),
    path('records/<int:pk>/delete/', views.record_delete, name='record-delete'),
    path('analytics/', views.analytics, name='analytics'),
]
