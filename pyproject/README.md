# Install
```
python3 -m venv ./venv
source venv/bin/activate
python3 -m pip install -r requirements.txt`
```

https://docs.djangoproject.com/en/3.2/intro/tutorial04/#use-generic-views-less-code-is-better


python3 manage.py makemigrations <module-name> # Generate a migration
python manage.py sqlmigrate <migration-name> <migration-id> # Check what Django is going to do
python3 manage.py check # Test applying migration
python3 manage.py migrate # Apply migration to database

python3 manage.py shell python shell plus import DJANGO_SETTINGS_MODULE which gives Django the import path to pyproject/settings.py

`HttpResponse(template.render(context, request))` or use `from django.shortcuts import render`
`try: Question.objects.get() except Question.DoesNotExist: raise Http404()` or `get_object_or_404(Question)`


Instead of a single function with `return render(request, 'polls/results.html', context)`
```
class ResultsView(generic.DetailView):
    model = Question # It auto-extracts the object (will be named "question") from here using the <pk> from the url
    template_name = 'polls/results.html'
```
You can override the context obj name with `context_object_name = 'latest_question_list'`


# Blog

    Blog homepage – displays the latest few entries.
    Entry “detail” page – permalink page for a single entry.
    Year-based archive page – displays all months with entries in the given year.
    Month-based archive page – displays all days with entries in the given month.
    Day-based archive page – displays all entries in the given day.
    Comment action – handles posting comments to a given entry.
