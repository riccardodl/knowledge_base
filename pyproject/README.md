# Install
```
python3 -m venv ./venv
source venv/bin/activate
python3 -m pip install -r requirements.txt`
```

https://docs.djangoproject.com/en/3.2/intro/tutorial04/#use-generic-views-less-code-is-better
https://docs.djangoproject.com/en/3.2/ref/models/expressions/#avoiding-race-conditions-using-f

python3 manage.py makemigrations <module-name> # Generate a migration
python manage.py sqlmigrate <migration-name> <migration-id> # Check what Django is going to do
python3 manage.py check # Test applying migration
python3 manage.py migrate # Apply migration to database

python3 manage.py shell python shell plus import DJANGO_SETTINGS_MODULE which gives Django the import path to pyproject/settings.py


# Blog

    Blog homepage – displays the latest few entries.
    Entry “detail” page – permalink page for a single entry.
    Year-based archive page – displays all months with entries in the given year.
    Month-based archive page – displays all days with entries in the given month.
    Day-based archive page – displays all entries in the given day.
    Comment action – handles posting comments to a given entry.
