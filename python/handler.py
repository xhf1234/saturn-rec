#!/usr/bin/env python

import tornado.web
from service import AppService, UserService
import utils
import json

appService = AppService()
userService = UserService()

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

class HomeHandler(BaseHandler):
    def get(self):
        users = userService.getRandomUsers(10)
        self.render('web/html/home.html', randomUsers = users)

class ApiHandler(BaseHandler):
    def _writeJson(self, json):
        self.write(json)
        self.set_header('Content-Type', 'application/json')
        self.set_status(200)
        self.flush()

class RecommendHandler(ApiHandler):
    def get(self, imei):
        apps = appService.getRecommendApps(imei)
        self._writeJson(utils.listToJson(apps))

class InstallHandler(ApiHandler):
    def get(self, imei):
        apps = appService.getInstallApps(imei)
        self._writeJson(utils.listToJson(apps))

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

class HandlebarsHandler(BaseHandler):
    def get(self, file):
        file = 'web/template/' + file[:-3]
        try:
            with open(file, 'r') as file:
                content = file.read()
                output = {"template": content}
                output = json.dumps(output)
                output = 'define(function (require, exports, module) {return ' + output + ';});'
                self.set_header('Content-Type', 'text/javascript')
                self.set_status(200)
                self.write(output)
                self.flush()
        except:
            self.set_status(404)
