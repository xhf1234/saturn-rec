#!/usr/bin/env python

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def _getFile(self, file):
        try:
            with open(file, 'r') as file:
                self.set_status(200)
                self.set_header('Content-Type', self._type())
                self.write(file.read())
                self.flush()
        except:
            self.set_status(404)

class _StaticHandler(BaseHandler):
    def get(self, file):
        file = 'web/%s/%s' %(self._staticDir(), file)
        super(_StaticHandler, self)._getFile(file)

class PageHandler(BaseHandler):
    def get(self):
        self.render('web/html/index.html')

class CssHandler(_StaticHandler):
    def _staticDir(self):
        return 'css'

    def _type(self):
        return 'text/css'

class JsHandler(_StaticHandler):
    def _staticDir(self):
        return 'js'

    def _type(self):
        return 'text/javascript'
