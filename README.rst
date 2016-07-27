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

    $ cd app
    $ npm install


Devlopement Setup
----------------------------------------------------------------------

We use ``webpack`` to build our boundled js file.

::

    $ cd app

    $ npm install -g webpack
    $ webpack  # or webpack --progress --colors --watch

    $ python ./server.py


Semantic UI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

We use semantic ui and self-shipped it in the ``./app/static/semantic``.

For developer note, following instruction is for building the semantic ui from
source::

    $ npm install -g gulp
    $ npm install semantic-ui
    $ cd semantic
    $ gulp build
    $ cp -r dist /path/to/app/static


Production Setup
----------------------------------------------------------------------

We recommand that using a reverse proxy (like nginx) for serving static
contents.

Please adjest the ``app/config.py``.

- ``DEBUG`` change into ``False``.

Then, make a webpack production build::

    $ cd app
    $ webpack -p
