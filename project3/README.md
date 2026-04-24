# CIS4930 Spring 2026 — Full-Stack Data Web Application with Django

## Group 08

| Name | Student ID |
|------|-----------|
| Alejandra McLetchie | am23ga |
| Raul Medrano | rem22r |
| Jake Serwe | js23g |
| Charlie Bleeze | cfb22 |

## Project Description

This Django web application explores a dataset of 500 Spotify tracks across 113 genres used in project 1, as well as the move API pipeline used in project 2. 

## Dataset & API

- **Dataset:** [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) — 500 sampled tracks with audio features
- **API:** [OMDB API](https://www.omdbapi.com/) — Movie data fetched and stored via Django management command

## Application Features

- **Homepage** (`/`) 
- **Track List** (`/records/`) 
- **Track Detail** (`/records/<pk>/`) 
- **Add Track** (`/records/add/`) 
- **Edit Track** (`/records/<pk>/edit/`) 
- **Delete Track** (`/records/<pk>/delete/`) 
- **Analytics Dashboard** (`/analytics/`)
- **Movie List** (`/movies/`)
- **Movie Search** (`/movies/search/`)
- **Movie CRUD** 
- **Fetch Data** (`/fetch/`)
- **Django Admin** (`/admin/`)

## Setup Instructions

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add a `SECRET_KEY` value (generate one with `python -c "import secrets; print(secrets.token_urlsafe(50))"`)

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed the database with Spotify CSV data**
   ```bash
   python manage.py seed_data
   ```

6. **Fetch movie data from OMDB API**
   ```bash
   python manage.py fetch_data
   ```

7. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## Screenshots

### Homepage


### Track List (with pagination)


### Analytics Dashboard


## Deployment Check

```
$ python manage.py check --deploy

System check identified some issues:

WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True.
?: (security.W018) You should not have DEBUG set to True in deployment.

System check identified 5 issues (0 silenced).
```

0 system-critical errors.

## Project Structure

```
project3/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── core/
│   ├── management/commands/
│   │   ├── seed_data.py
│   │   └── fetch_data.py
│   ├── migrations/
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── list.html
│   │   ├── detail.html
│   │   ├── form.html
│   │   ├── confirm_delete.html
│   │   └── analytics.html
│   ├── static/css/style.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
├── data/raw/sample.csv
├── .env.example
├── .gitignore
├── requirements.txt
├── Procfile
├── runtime.txt
├── manage.py
└── README.md
```

## Technologies Used

- Python 3.13
- Django 
- pandas
- requests
- Bootstrap 
- Chart.js
- SQLite (Django ORM)
- python-decouple
- gunicorn + whitenoise
