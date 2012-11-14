#!/usr/bin/env python
# encoding=utf8

import codecs
from data import App
import utils

def importApp():
    input = codecs.open('../data/app.data', 'r', 'gbk');

    apps = []
    for line in input.readlines():
        line = line.encode('utf8')
        l = line.split('\t', 1)
        package = l[0].strip()
        name = l[1].strip()
        apps.append(App(package, name))
    print utils.listToString(apps)

if __name__ == '__main__':
    importApp()
    exit(0)
