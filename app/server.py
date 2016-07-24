import logging

import jinja2
from tornado import ioloop
from tornado.template import Loader
from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado_jinja2 import Jinja2Loader

import config

log = logging.getLogger('iottalk-gui')


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


def mkapp():
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(config.TEMPLATE_DIR))

    return Application(
        (
            (r'/', MainHandler),
            (r'/static/(.*)', StaticFileHandler,),
        ),
        autoreload=config.DEBUG,
        debug=config.DEBUG,
        static_path=config.STATIC_DIR,
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
