from pyramid.config import Configurator
from mongoengine import connect


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    # mongo settings
    url_str = settings.get('mongo_uri', 'mongodb://localhost:27017/topicExample')
    connect('topicExample', host=url_str)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pyforum_view', '/list')
    config.add_route('pyforum_add', '/add')
    config.add_route('pyforum_delete', '/delete/{id}')
    config.scan()
    return config.make_wsgi_app()
