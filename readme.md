To setup a dev environment:

```bash
# Clone the repository

# enter the repository
cd Management-system-with-django

# activate the virtual environnement 
venv/scripts/activate

# install django
pip install django

# Run the local server
python manage.py runserver
```

To create a superuser account:

```bash
python manage.py createsuperuser

# enter superuser part
python manage.py runserver

http://127.0.0.1:8000/admin

```

superuser i created: 
Username : admin
Email address: admin@admin.com
Password: admin123?