:tocdepth: 2

First Django App
==================

A step-by-step guide to creating a simple web application that displays House office expenditure data.

You will learn just enough about the `Django <https://www.djangoproject.com/>`_ framework to design database tables, load in data and display it at different URLs based on the data.

What you will make
------------------

This tutorial will guide you through creating a custom Django app displaying information about `official House office expenditures <https://www.house.gov/the-house-explained/open-government/statement-of-disbursements>`_.

About the authors
-----------------

This guide was developed by Derek Willis of the University of Maryland's Philip Merrill College of Journalism for use in JOUR328/JOUR628, the News Applications class.

Prelude: Prerequisites
----------------------

Before you can begin, your computer needs the following tools installed
and working.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`_ to work with plain text files
3. Version 3.8 or higher of the `Python <https://www.python.org/downloads/>`_ programming language
4. The `pipenv <https://pipenv.pypa.io/en/latest/>`_ package and virtual environment manager for Python
5. `Git <http://git-scm.com/>`_ version control software and an account at `GitHub.com <http://www.github.com>`_

.. warning::

    Stop and make sure you have all these tools installed and working properly. Otherwise, `you're gonna have a bad time <https://www.youtube.com/watch?v=ynxPshq8ERo>`_.

.. _command-line-prereq:

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to open a window that lets you type in commands. Different operating systems give this tool slightly different names, but they all have some form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the "command prompt." Here are `instructions <https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/>`_. On Apple computers, you open the `"Terminal" application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_. Ubuntu Linux comes with a program of the `same name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`_.


Text editor
~~~~~~~~~~~

A program like Microsoft Word, which can do all sorts of text formatting
such as change the size and color of words, is not what you need. Do not
try to use it below.

You need a program that works with simple `"plain text"
files <https://en.wikipedia.org/wiki/Text_file>`__, and is therefore
capable of editing documents containing Python code, HTML markup and
other languages without dressing them up by adding anything extra. Such
programs are easy to find and some of the best ones are free, including
those below.

For Windows, I recommend installing
`Notepad++ <https://notepad-plus-plus.org/>`__. For Apple computers, try
`Atom <https://atom.io/>`__.
In Ubuntu Linux you can stick with the pre-installed
`gedit <https://help.ubuntu.com/community/gedit>`__ text editor.

Python
~~~~~~

Python is a computer programming language, like many others you may have heard of such as Ruby or PHP or Java. It is free and open source. We'll be installing Python 3 in a virtual environment, so it doesn't matter what version you have installed currently.

For Mac
^^^^^^^

If you are using Mac OSX, Python version 2.7 is probably already installed, but we'll be using Python 3. To install that, we'll be using `Homebrew <https://docs.python-guide.org/starting/install3/osx/#install3-osx>`_.

To install Python via Homebrew, you can run the following code:

.. code-block:: bash

    $ brew install python

.. note::

    You'll note that the example above begins with a "$". You do not need to type this. It is only a generic symbol
    commonly used by geeks to indicate a piece of code should be run from the command line. On Windows, this prompt could even look quite different, likely starting with a phrase like ``C:\``.

You should see something like this after you hit enter:

.. code-block:: bash

    $ python -V
    Python 3.9.7


For Windows
^^^^^^^^^^^

Windows people should follow the instructions `here <https://docs.python-guide.org/starting/install3/win/#install3-windows>`_.

.. _command-line-pipenv:

pipenv
~~~~~~~~~~~~~~~~~~

The `pipenv package manager <https://pipenv.pypa.io/>`_ makes it easy to install open-source libraries that expand what you're able to do with Python. Later, we will use it to install everything needed to create a working web application.

Verify pipenv is installed with the following command:

.. code-block:: bash

    $ pipenv -v

If you get and error, that means you don't have pipenv installed. You can get it by following `these instructions <https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv>`_.

Act 1: Hello Django
-------------------

Start at our first-django-app directory.

.. code-block:: bash

    $ mkdir first-django-app
    $ cd first-django-app

Create a new development environment with pipenv, specifying the version of python:

.. code-block:: bash

    # You don't have to type the "$" It's just a generic symbol
    # geeks use to show they're working on the command line.
    $ pipenv --python=python3

Then activate it (it's like turning on the power):

.. code-block:: bash

    $ pipenv shell


Use ``pipenv`` on the command line to install `Django <https://www.djangoproject.com/>`_, a Python "framework"
we'll use to put together our website.

.. code-block:: bash

    $ pipenv install Django

Now use Django's ``django-admin`` command to create a new project that will be organized according to the framework's rules. We'll creatively call it "project".

.. code-block:: bash

    $ django-admin startproject project

Now jump into the project and we'll start setting it up.

.. code-block:: bash

    $ cd project

.. note::

    Run the ``ls`` command (``dir`` on Windows), which lists the files in your current location. Wonder what all those weird files are in your new directory? We'll only need a couple for this tutorial, but you can read about all of them in the `official Django documentation <https://docs.djangoproject.com/en/1.10/intro/tutorial01/#creating-a-project>`_.

There is a lot of `configuration <https://docs.djangoproject.com/en/4.0/intro/tutorial02/#database-setup>`_ that could be done at this point, but we're going to advance with all of the Django defaults in place.

The first step is creating your database, which will appear as a new `SQLite <https://en.wikipedia.org/wiki/SQLite>`_ file named ``db.sqlite3``.

To do that, we will start using the ``manage.py`` file created by ``startproject``. It is a utility belt we can use to make Django a wide range of things. The command we want now, ``migrate``, can create database tables.

.. code-block:: bash

    $ python manage.py migrate

Fire up Django's built-in web server.

.. code-block:: bash

    $ python manage.py runserver

Visit `localhost:8000 <http://localhost:8000>`_ in your browser to see Django in action. Here's what you should see.

.. image:: /_static/hello-django.jpg

Congratulations. You've installed Django and have a blank site started up and running. Now the real work begins.

Act 2: Hello models
-------------------

Now we create our app. In Django terms, an app is a collection of files that does something, like publish a blog or store public records. A project, like we made above, collects those apps and organizes them into a working website.

You can create a new app with Django's ``startapp`` command. Since we are aiming to make a list of people invited to join the academy, naming this one isn't too hard.

Return to your terminal and hit the combination of ``CTRL-C``, which will terminal your test server and return you to the command line. Then use our friend ``manage.py`` to create our app.

.. code-block:: bash

   $ python manage.py startapp expenses

There should now be a new ``expenses`` folder in your project. If you look inside you will see that Django created a series of files common to every app.

.. code-block:: txt

  expenses/
      __init__.py
      admin.py
      apps.py
      migrations/
      models.py
      tests.py
      views.py

We will only be using two of them in this tutorial. The file called ``models.py`` is where we will design our database tables. Another called ``admin.py`` is where we will configure the panels where reporters will be able to enrich the source data.

But before we do any of that, we need to configure our project to include our new app. Use your text editor to open the file ``settings.py`` in the ``project`` directory. Add our app, ``academy``, to the ``INSTALLED_APPS`` list you find there.

.. code-block:: python
  :emphasize-lines: 8

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'expenses',
    )

.. note::

    Python, like most programming languages, is very strict. When you add a new word to a list, as we did above, it always needs to be followed by a comma and surrounded by quotes. The indentations are also very stict and need to be consistent from line to line. Also, lines starting with ``#`` or surrounding by `"""` quotes are comments that will not be run as code and are instead there only as documentation.

Next open up the ``models.py`` file in the ``expenses`` app's directory. Here we will use Django's built-in `models <https://docs.djangoproject.com/en/4.0/topics/db/models/>`_ system to design a database table to hold the source data.

Each table is defined using a Python `class <http://www.learnpython.org/en/Classes_and_Objects>`_ that inherits special powers `from Django <https://docs.djangoproject.com/en/dev/topics/db/models/>`_. Those special powers allow it to synchronize with an underlying database. Our work begins by creating our class and naming it after the data we'll put inside.

.. code-block:: python
  :emphasize-lines: 4

  from django.db import models

  # Create your models here.
  class Summary(models.Model):

.. note::

    Don't know what a class is? Don't stress out about it. It's a little tricky to explain, but a class is basically a blueprint for designing how information in your code is structured. In our case, we're creating a blueprint that will link up our data with a traditional database table (this is often called a schema).

Next, like any good database table, it needs some fields.

If you open `the source CSV <https://github.com/dwillis/first-django-app-umd/blob/master/project/summary.csv>`_, you will see that is has eight columns.

Django has some `fancy tricks <https://docs.djangoproject.com/en/4.0/ref/models/fields/>`_ for defining fields depending on what kind of data they hold. Now we'll use the ``CharField`` to expand our models to hold the bioguide, office, program and category data from our source. It just so happens, that CharFields have a maximum length that must always be set. We're going to pick a couple big numbers for that.

.. code-block:: python
  :emphasize-lines: 5-6

    from django.db import models

    # Create your models here.
    class Summary(models.Model):
        bioguide_id = models.CharField(max_length=7)
        office = models.CharField(max_length=500)
        program = models.CharField(max_length=500)
        category = models.CharField(max_length=500)
        year_to_date = models.DecimalField(max_digits=20, decimal_places=2)
        amount = models.DecimalField(max_digits=20, decimal_places=2)
        year = models.IntegerField()
        quarter = models.IntegerField()

.. note::

    Watch out. You'll need to carefully indent your code according to Python's very `strict rules <https://www.geeksforgeeks.org/indentation-in-python/>`_ for this to work.

Congratulations, you've written your first model. But it won't be created as a real table in your database until you run what Django calls a "migration." That's just a fancy word for syncing our models with our database.

Make sure to save your ``models.py`` file. Then we'll ``manage.py`` to prepare the changes necessary to create your new model.

.. code-block:: bash

    $ python manage.py makemigrations expenses

Now run the ``migrate`` command to execute it.

.. code-block:: bash

    $ python manage.py migrate expenses

That's it. You've made a database table. Let's do the same for the detail expense file. There are a few more fields but many of them are the same as the `Summary` model.

.. code-block:: python
  :emphasize-lines: 13

  from django.db import models

  class Summary(models.Model):
      bioguide_id = models.CharField(max_length=7)
      office = models.CharField(max_length=500)
      program = models.CharField(max_length=500)
      category = models.CharField(max_length=500)
      year_to_date = models.DecimalField(max_digits=20, decimal_places=2)
      amount = models.DecimalField(max_digits=20, decimal_places=2)
      year = models.IntegerField()
      quarter = models.IntegerField()

  class Detail(models.Model):
      bioguide_id = models.CharField(max_length=7)
      office = models.CharField(max_length=500)
      quarter = models.CharField(max_length=1)
      program = models.CharField(max_length=500)
      category = models.CharField(max_length=500)
      sort_sequence = models.CharField(max_length=500)
      date = models.DateField(blank=True, null=True)
      transcode = models.CharField(max_length=15)
      recordid = models.CharField(max_length=500, blank=True, null=True)
      payee = models.CharField(max_length=500)
      start_date = models.DateField(blank=True, null=True)
      end_date = models.DateField(blank=True, null=True)
      purpose = models.CharField(max_length=500)
      amount = models.DecimalField(max_digits=20, decimal_places=2)
      year = models.IntegerField()

Make sure to save your ``models.py`` file. Then we'll ``manage.py`` to prepare the changes necessary to create your new model.

.. code-block:: bash

    $ python manage.py makemigrations expenses

Now run the ``migrate`` command to execute it.

.. code-block:: bash

    $ python manage.py migrate expenses

Now you've made two database tables!

Act 3: Hello loader
-------------------

Our next challenge is to load the source CSV file into the model.

We are going to do this using Django's system for `management commands <https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/>`_. It allows us to make our own ``manage.py`` commands like ``migrate`` and ``startapp`` that take advantage of Django's bag of tricks and interact with the database.

To do this, add a ``management/commands`` directory in our expenses app, complete with empty ``__init__.py`` files required by Python. You can do this in your operating system's file explorer, or on the command line. From a Linux or OSX prompt that would look something like this.

.. code-block:: bash

  # The -p flag here makes both new directories
  $ mkdir -p expenses/management/commands
  # This creates the empty files on Macs or in Linux
  $ touch expenses/management/__init__.py
  $ touch expenses/management/commands/__init__.py

From Windows something more like this:

.. code-block:: bash

  # If you're in Windows create them with your text editor
  $ start notepad++ expenses/management/__init__.py
  $ start notepad++ expenses/management/commands/__init__.py

When you're done the app's directory should look something like this.

.. code-block:: txt

  expenses/
      __init__.py
      admin.py
      apps.py
      models.py
      management/
          __init__.py
          commands/
              __init__.py
      migrations/
      tests.py
      views.py

Create a new file in the ``management/commands`` directory where the new command will go. Let's call it ``load_summary.py``.

.. code-block:: bash

  # Mac or Linux
  $ touch expenses/management/commands/load_summary.py
  # Windows
  $ start notepad++ expenses/management/commands/load_summary.py

Open it up and paste in the skeleton common to all management commands.

.. code-block:: python

  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print("Loading CSV")

Running it is as simple as invoking its name with ``manage.py``.

.. code-block:: bash

  $ python manage.py load_summary

Download `the source CSV file  <https://raw.githubusercontent.com/dwillis/first-django-app-umd/master/project/summary.csv>`_ from GitHub and store it in your base directory next to ``manage.py``.

Return to the management command and introduce Python's built-in `csv module <https://docs.python.org/3/library/csv.html>`_, which can read and files CSV files.

.. code-block:: python
  :emphasize-lines: 1

  import csv
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print("Loading CSV")

Next add a variable beneath the print command that contains the path to where you've saved the CSV file. If you've saved it next to ``manage.py``, that is as simple as starting off with "./".

.. code-block:: python
  :emphasize-lines: 8

  import csv
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print("Loading CSV")
          csv_path = "./summary.csv"

.. note::

    In case you don't already know, a “variable” is a fancy computer programming word for a named shortcut where we save our work as we go.

Now access the file at that path with Python's built-in ``open`` function.

.. code-block:: python
  :emphasize-lines: 9

  import csv
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print "Loading CSV"
          csv_path = "./summary.csv"
          csv_file = open(csv_path, 'r')

Feeding the file object it creates into the ``csv`` module's ``DictReader`` will return a list with each row read to work with.

.. code-block:: python
  :emphasize-lines: 10

  import csv
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print "Loading CSV"
          csv_path = "./summary.csv"
          csv_file = open(csv_path, 'r')
          csv_reader = csv.DictReader(csv_file)

Create a loop that walks through the list, printing out each row as it goes by.

.. code-block:: python
  :emphasize-lines: 11-12

  import csv
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print "Loading CSV"
          csv_path = "./summary.csv"
          csv_file = open(csv_path, 'r')
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
              print(row)

Run it to see what we mean.

.. code-block:: bash

  $ python manage.py load_summary

Import our model into the command and use it to save the CSV records to the database.

.. code-block:: python
  :emphasize-lines: 2,13-17

  import csv
  from expenses.models import Summary
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print "Loading CSV"
          csv_path = "./summary.csv"
          csv_file = open(csv_path, 'r')
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
              obj = Summary.objects.create(
                  bioguide_id=row['BIOGUIDE_ID'],
                  office=row['OFFICE'],
                  program=row['PROGRAM'],
                  category=row['CATEGORY'],
                  year_to_date=row['YTD'],
                  amount=row['AMOUNT'],
                  year=row['YEAR'],
                  quarter=row['QUARTER']
              )
              print(obj)

Run it again and you've done it. The data from the summary CSV is loaded into the database.

.. code-block:: bash

  $ python manage.py load_summary

You can do the same for the detail file - the same steps, creating a ``load_detail.py`` file in the ``management/commands`` directory the same way you did for the summary file, along with the code to load the CSV.

.. code-block:: python
  :emphasize-lines: 2,9,21

  import csv
  from expenses.models import Detail
  from django.core.management.base import BaseCommand

  class Command(BaseCommand):

      def handle(self, *args, **options):
          print("Loading CSV")
          csv_path = "./detail.csv"
          csv_file = open(csv_path, 'r')
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
              obj = Detail.objects.create(
                  bioguide_id=row['BIOGUIDE_ID'],
                  office=row['OFFICE'],
                  quarter=row['QUARTER'],
                  program=row['PROGRAM'],
                  category=row['CATEGORY'],
                  sort_sequence=row['SORT SEQUENCE'],
                  date=row.get('DATE') or None,
                  transcode=row['TRANSCODE'],
                  recordid=row['RECORDID'].strip(),
                  payee=row['PAYEE'],
                  start_date=row.get('START DATE') or None,
                  end_date=row.get('END DATE') or None,
                  purpose=row['PURPOSE'],
                  amount=row['AMOUNT'],
                  year=row['YEAR']
              )
              print(obj)

Note how for the date fields we're using a specific syntax that tries to grab the value for that key and if there's any problem (such as an empty string instead of a date) we just use ``None`` instead.

Act 4: Hello admin
------------------

One of Django's unique features is that it comes with a custom administration that allows users to view, edit and create records. To see it in action, create a new superuser with permission to edit all records.

.. code-block:: bash

    $ python manage.py createsuperuser

Then fire up the Django test server.

.. code-block:: bash

    $ python manage.py runserver

And visit `localhost:8000/admin/ <http://localhost:8000/admin/>`_ and log in using the credentials you just created.

.. image:: /_static/hello-admin-login.png

Without any additional configuration you will see administration panels for the apps installed with Django by default.

.. image:: /_static/hello-admin-noconfig.png

Adding panels for your own models is done in the ``admin.py`` file included with each app. Open ``academy/admin.py`` to start in.

.. code-block:: python

  from django.contrib import admin
  from expenses.models import Summary

  admin.site.register(Summary)

Now reload `localhost:8000/admin/ <http://localhost:8000/admin/>`_ and you'll see it added to the index app list.

.. image:: /_static/hello-admin-module.png

Click on "Summarys" and you'll see all the records we loaded into the database as a list.

.. image:: /_static/hello-admin-list.png

Configure the columns that appear in the list.

.. code-block:: python
  :emphasize-lines: 4-7

  from django.contrib import admin
  from expenses.models import Summary

  class SummaryAdmin(admin.ModelAdmin):
      list_display = ("office", "program", "category", "amount")

  admin.site.register(Summary, SummaryAdmin)

Reload.

.. image:: /_static/hello-admin-columns.png

Add a filter.

.. code-block:: python
  :emphasize-lines: 6

  from django.contrib import admin
  from expenses.models import Summary

  class SummaryAdmin(admin.ModelAdmin):
      list_display = ("office", "program", "category", "amount")
      list_filter = ("category", "program")

  admin.site.register(Summary, SummaryAdmin)

Reload.

.. image:: /_static/hello-admin-filter.png

And now a search.

.. code-block:: python
  :emphasize-lines: 7

  from django.contrib import admin
  from expenses.models import Summary

  class SummaryAdmin(admin.ModelAdmin):
      list_display = ("office", "program", "category", "amount")
      list_filter = ("category", "program")
      search_fields = ("program",)

  admin.site.register(Summary, SummaryAdmin)

Reload.

.. image:: /_static/hello-admin-search.png

Take a moment to search, filter and sort the list to see how things work. Now we can add a similar admin for the ``Detail`` objects:

.. code-block:: python
  :emphasize-lines: 2, 8-11, 13

  from django.contrib import admin
  from expenses.models import Summary, Detail

  class SummaryAdmin(admin.ModelAdmin):
      list_display = ("office", "program", "category", "amount")
      list_filter = ("category", "program")
      search_fields = ("program",)

  class DetailAdmin(admin.ModelAdmin):
      list_display = ("office", "program", "category", "payee", "purpose", "amount")
      list_filter = ("category", "program", "purpose")
      search_fields = ("program", "payee")

  admin.site.register(Summary, SummaryAdmin)
  admin.site.register(Detail, DetailAdmin)


Act 5: Hello Views
---------------------

Now you're ready to show your data to people who can't (and shouldn't) login to your Django app. We do that using ``views``, which are invoked when a specific URL is loaded.

Open expenses/views.py and put the following code in it:

.. code-block:: python

  from django.http import HttpResponse

  def index(request):
    return HttpResponse("Hello, world. You're at the expenses index.")

This is the simplest view we can write. When that view is triggered, it will return that text to the browser just as it is. But we need to tie it to a specific url. For that we can create a new file in the expenses directory called ``urls.py`` and add the following code to it:

.. code-block:: python

  from django.urls import path

  from . import views

  urlpatterns = [
    path('', views.index, name='index'),
  ]

This first imports a function that helps Django connect urls to views. It then imports the contents of our views.py file and finally defines a pattern: if a user goes to the root url, that means that the ``index`` view gets called. All of that occurs in project/expenses/urls.py.

But we have more urls for our project, including the admin urls. Check out the ``urls.py`` in the project/project directory, and add this to it:

.. code-block:: python
  :emphasize-lines: 3,6

  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
    path('expenses/', include('expenses.urls')),
    path('admin/', admin.site.urls),
  ]

This ``urls.py`` organizes _all_ of the urls we could have for this entire project (we might decide to get expansive and include other congressional data). We _include_ the url we defined that is specific to the expenses app.

Now go to http://127.0.0.1:8000/expenses/

.. image:: /_static/hello-expenses.png
