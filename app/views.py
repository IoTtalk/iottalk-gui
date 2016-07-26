from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.render('base.html')


class ProjectHandler(RequestHandler):
    def get(self):
        pass
