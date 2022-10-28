from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid.session import UnencryptedCookieSessionFactoryConfig

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI aplicaci�n.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    # Session Configuration
    my_session_factory = UnencryptedCookieSessionFactoryConfig('session_key_generator')
    config = Configurator(settings=settings, session_factory=my_session_factory)
#    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
