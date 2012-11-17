#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import os
from handler import *

settings = {
    'debug': True
}

application = tornado.web.Application([
    (r'/', HomeHandler),
    (r'/home', HomeHandler),
    (r'/api/recommend/([^/]+)', RecommendHandler),
    (r'/api/install/([^/]+)', InstallHandler),
    (r'/(.+\.css)$', CssHandler),
    (r'/(.+\.handlebars\.js)$', HandlebarsHandler),
    (r'/(.+\.js)$', JsHandler)
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
