#!/usr/bin/env python

def listToString(l):
    return '[%s]' % '\n '.join(map(str, l))

def listToJson(l):
    r = '['
    first = True
    for item in l:
        if not first:
            r = r + ','
        r = r + item.toJson()
        first = False
    r = r + ']'
    return r
