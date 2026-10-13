# Shop API

Proste API REST napisane w Pythonie i Django.

## Uruchomienie

```bash
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data
python manage.py createsuperuser
python manage.py runserver