# Django Search Application

![Screenshot](./public/app_ss.png)

## Requirements

- Python 3.x
- Django 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rohitdhas/django-search-app.git
   ```

2. Change into the project directory:

   ```bash
   cd django-search-app
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Load data from the CSV file into the SQLite database:

   ```bash
   python manage.py load_data
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and visit `http://localhost:8000` to access the application.
