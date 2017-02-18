# Django Dev Sprint at Pycon Pune 2017

[Contributing to Django](https://docs.djangoproject.com/en/dev/internals/contributing/) and [Advice for new contributors](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/) are good pointers

## Working with Django code locally

### Setting up Django
1. `git clone git@github.com:django/django.git`
1. `python setup.py install` which will install django on your virtualenv
1. `mkvirtualenv -p /usr/local/bin/python3.4 django110` this will ensure Django 2 works nicely with Python 3

### Building Documentation

1. `cd django/docs`
1. `pip install Sphinx`
1. `make html`
1. `open _build/html/index.html` to see documentation


### Building Tests
1. `cd django/tests`
1. `python runtests.py`


