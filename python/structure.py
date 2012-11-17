#!/usr/bin/env python

class FIFOCache(object):
    
    def __init__(self, size = 100):
        self.size = size
        self._list = []
    
    def put(self, id, data):
        self._list.append((id, data))
        if (len(self._list) > self.size):
            self._list.pop(0)

    def get(self, id):
        for item in self._list:
            if item[0] == id:
                return item[1]
        return None
