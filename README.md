pyramid-forum
=============

Simple forum with Pyramid and MongoDB

Hand's On Pyramid Forum

Requirements - Python >=2.7 , virtualenv, virtualenvwrapper(*op)

    $ mkvirtualenv pyforum
    $ pip install pyramid pyramid_jinja2 nose WebTest coverage FormEncode Jinja2 coverage mongoengine pymongo pyramid-debugtoolbar pyramid-jinja2
    $ git clone https://github.com/tgonzales/pyramid-forum.git
    $ cd pyramid-forum
    $ python setup.py develop
    $ mongod --dbpath ~/data/db #your path db
    $ nosetests pyforum
    $ pserve development.ini --reload
    browser://localhost:6543

