from django.shortcuts import render
from django.views.generic import TemplateView

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
