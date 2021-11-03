# Contextualise
Contextualise officially supports Python 3.6–3.9.

If you have `Git <https://git-scm.com/>`_ installed on your system, it is possible to install the development version
of Contextualise.

Certain build prerequisites need to be met including the presence of a C compiler, the Python
header files, the ``libpq`` header files and the ``pg_config`` program as outlined, here: `Build
prerequisites <http://initd.org/psycopg/docs/install.html#build-prerequisites>`_.

Then do::

    $ git clone https://github.com/anthcp-infocom/Contextualise
    $ cd contextualise
    $ pip install -e .

The ``pip install -e .`` command allows you to follow the development branch as it changes by creating links in the
right places and installing the command line scripts to the appropriate locations.

Then, if you want to update Contextualise at any time, in the same directory do::

    $ git pull

`TopicDB`_, the topic maps engine on top of which Contextualise is built is regularly updated. However, the version
of TopicDB published on `PyPI <https://pypi.org/project/topic-db/>`_ could lag behind.

    $ cd topic-db
    $ pip install -e .

After having installed Contextualise, you would have to separately install and configure the PostgreSQL database. Brief
instructions on how to do so are provided, here:
```
sudo -i -u postgres
psql
CREATE USER databasuser WITH PASSWORD 'password';
CREATE DATABASE databasename OWNER databasuser;
\q
psql -h localhost -U databasuser -d databasename -a -f topicmap-definition.sql
exit
```

You need to ensure that the database username, password and database name match with the ``settings.ini`` file in the project's root folder.

Finally, to run the application in **development** mode you need to change to the project's top-level directory and set
two environment variables followed by running the ``flask`` command with the ``run`` parameter::

    $ export FLASK_APP=contextualise
    $ export FLASK_ENV=development
    $ flask run

You should see something similar to the following in the terminal::

    * Serving Flask app "contextualise" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 521-258-444
