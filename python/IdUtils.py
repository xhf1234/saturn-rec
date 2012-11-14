#!/usr/bin/env python
import md5

def genId(str):
    m = md5.new()
    m.update(str)
    return (int(m.hexdigest(), 16)%18446744073709551615)
