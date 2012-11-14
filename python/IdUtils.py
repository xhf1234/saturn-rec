#!/usr/bin/env python
import md5

idCache = {}

def genId(str):
    if str in idCache:
        return idCache[str]
    m = md5.new()
    m.update(str)
    id = (int(m.hexdigest(), 16)%18446744073709551615)
    idCache[str] = id
    return id
