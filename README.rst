.. -*- coding: utf-8 -*-

========================
identity manager project
========================

The ``identity manager project`` is an identity manager project to show the
development practices currenlty in use in <ahref.

It is a skeleton of a ``flask`` application, but the general rules are meant for
all projects.


Developer Instructions
======================


Requirements
------------

This guide assumes that you develop the ``identity manager project`` on a
``Debian/GNU Linux`` version ``Wheezy``.

.. code:: sh

    sudo apt-get install python-virtualenv \
    mongodb-server


Virtualenv
----------

There are several tools that help to manage python virtualenvs.  If you are
already familiar with ``virtualenvwrapper`` you can use it.  If not just follow
the following suggestions:

.. code:: sh

    cd
    mkdir ve
    cd ve
    vitutualenv identity manager project-ve
    . identity manager project-ve/bin/activate

.. warning::

    Remember to activate the virtualenv every time you start developing.


Source code
-----------

The source code is manage with ``git`` using the ``git-flow`` work-flow.

You should have an account with writing privileges.

.. code:: sh

    cd
    mkdir dev
    cd dev
    git clone git@git.ahref.eu:misc/identity manager.git
    cd identity manager
    git checkout -b develop origin/develop


Development
-----------

The ``identity manager project`` is developed as a python packages.  The
``develop`` command will download and install the requirements.

.. code:: sh

    python setup.py develop

You can start developing following the issues for your milestone.


Testing
-------

``identity manager project`` follow a strict testing procedure.  Before every
commit you must check that the test pass and that the source code respect the
best practices defined by the ``python`` community.

.. code:: sh

    python setup.py test
    python setup.py flake8

An improved test runner is:

.. code:: sh

    nosetests -c nose.cfg

This will open a ``ipdb`` shell in case of errors and failures and provide a
coverage report.


Documentation
-------------

The developer documentation is made with ``sphinx`` and in particular with
``sphinxcontrib.autohttp.flask``.  A quick start:

.. code:: sh

    cd docs
    make singlehtml
    xdg-open build/singlehtml/index.html


Manage command
--------------

For convenience other flask related commands are available, just run ``im``
to see the list.


Instructions for the system administrator
=========================================


Deploy
------

Requirements:

.. code:: sh

    sudo apt-get install uwsgi uwsgi-plugin-python


Loading the initial data: to load arbitrary data, in the virtualenv you can run:

.. code:: sh

    im load_demo_data --from-file FILE.json


Example for running the app:

.. code:: sh

    uwsgi_python \
	--env IM_SETTINGS=/srv/web/identitymanager/etc/config.py \
        --socket /var/run/identity-uwsgi.sock \
        --module IdentityManager:app \
        --virtualenv /home/daniele/ahref/ve/identitymanager1/

We use the best practices with the environment variable IM_SETTINGS:
http://flask.pocoo.org/docs/config/#development-production

Example for nginx.conf::

    http {
	server {
	    listen 8001;
	    server_name identity-manager.be.ahref.eu;
	    location / { try_files $uri @identitymanager; }
	    location @identitymanager {
		include /etc/nginx/uwsgi_params;
		uwsgi_pass unix:/var/run/identity-uwsgi.sock;
	    }
	}
    }


Optionally we can also start and manage uwsgi with supervisor(d).

