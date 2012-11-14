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
