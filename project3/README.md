How to get project running:

1. Initialize the venv
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Prep the database
   ```bash
   python manage.py migrate
   ```

4. Fetch data from API
 ```bash
   python manage.py fetch_data
   ```

5. Run app via django
   ```bash
   python manage.py runserver
   ```
