#!/usr/bin/env python

import IdUtils

class App(object):
    def __init__(self, package, name, id=None):
        self.name = name
        self.package = package
        self.id = id 
        #generate id if necessary
        self.genId()

    def genId(self):
        """ generate id if necessary, as a digest value of self.package"""
        if self.id is None:
            self.id = IdUtils.genId(self.package)
        return self.id

    def __str__(self):
        return "[id:%d\tpackage:%s\tname:%s]" % (self.id, self.package, self.name) 

    def toJson(self):
        return '{"id":%d, "package":"%s", "name":"%s"}' % (self.id, self.package, self.name)

class RecApp(object):
    def __init__(self, app, score):
        self.app = app
        self.score = score

    def __str__(self):
        return "app: %s\tscore: %.1f" % (str(self.app), self.score) 

    def toJson(self):
        return '{"app": %s, "score":%.1f}' % (self.app.toJson(), self.score)
    
        
class User(object):
    def __init__(self, imei, id=None):
        self.imei = imei 
        self.id = id 
        #generate id if necessary
        self.genId()

    def genId(self):
        """ generate id if necessary, as a digest value of self.imei"""
        if self.id is None:
            self.id = IdUtils.genId(self.imei)
        return self.id

    def __str__(self):
        return "[id:%d\timei:%s]" % (self.id, self.imei) 

class Rec(object):
    def __init__(self, uid, aid, score):
        self.uid = uid
        self.aid = aid
        self.score = score
    
class Install(object):
    def __init__(self, uid, aid):
        self.uid = uid
        self.aid = aid
