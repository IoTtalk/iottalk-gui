import logging
import os

import jinja2

from tornado import ioloop
from tornado.gen import coroutine
from tornado.template import Loader
from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado_jinja2 import Jinja2Loader

import config

log = logging.getLogger('iottalk-gui')


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class MultiStaticFileHandler(StaticFileHandler):
    def initialize(self, *args, paths=None, **kwargs):
        super(type(self), self).initialize(*args, **kwargs)
        self.paths = paths if paths else [self.root]

    # @coroutine
    def get(self, *args, **kwargs):
        path = args[0]
        roots = [p for p in self.paths
                    if os.path.exists(os.path.join(p, path))
                ] or [self.root]

        for root in roots:
            self.root = root
            return super(type(self), self).get(*args, **kwargs)


def mkapp():
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(config.TEMPLATE_DIR),
    )

    url_conf = (
        (r'/', MainHandler),
    )

    if config.DEBUG:
        url_conf += (
            (r'/static/(.*)', MultiStaticFileHandler),
        )

    return Application(
        url_conf,
        autoreload=config.DEBUG,
        debug=config.DEBUG,
        static_path=config.STATIC_DIRS[0],
        static_handler_args={'paths': config.STATIC_DIRS},
        static_handler_class=MultiStaticFileHandler,
        template_loader=Jinja2Loader(jinja2_env),
        template_path=config.TEMPLATE_DIR,
    )


def main():
    if config.DEBUG:
        logging.basicConfig(level=logging.DEBUG)

    app = mkapp()
    app.listen(config.HTTP_PORT)

    log.info('Start GUI server on port %s', config.HTTP_PORT)
    try:
        ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
