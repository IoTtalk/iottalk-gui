IoTtalk GUI
===============================================================================

*This repo is a work in progress.*

The graphical user interface for IoTtalk system.


Install Dependencies
----------------------------------------------------------------------

We have a file ``requirements.txt`` for denoting the backend dependencies.
We use ``tonado`` as our webapp framework and server::

    $ pip install -r ./requirements.txt

For the static contents, we use NPM's ``package.json``::

    $ npm install -g gulp
    $ npm install --prefix ./app/static/vendor

Biuld semantic ui::

    $ cd ./app/static/vendor/semantic
    $ gulp build


Devlopement Setup
----------------------------------------------------------------------

::

    $ python app/server.py


Production Setup
----------------------------------------------------------------------

We recommand that using a reverse proxy (like nginx) for serving static
contents.

Please adjest the ``app/config.py``.

- ``DEBUG`` change into ``False``.
