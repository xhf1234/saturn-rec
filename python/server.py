#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import os
from handler import PageHandler, CssHandler, JsHandler

settings = {
    'debug': True
}

application = tornado.web.Application([
    (r'/', PageHandler),
    (r'/(.+\.css)$', CssHandler),
    (r'/(.+\.js)$', JsHandler)
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
