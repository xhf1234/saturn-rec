#!/usr/bin/env python
# encoding=utf8

import codecs
from data import App
import utils
from dbStorage import AppDbStorage

appStore = AppDbStorage()

def importApp():
    input = codecs.open('../data/app.data', 'r', 'gbk');

    apps = []
    for line in input.readlines():
        line = line.encode('utf8')
        l = line.split('\t', 1)
        package = l[0].strip()
        name = l[1].strip()
        apps.append(App(package, name))
    for app in apps:
        appStore.save(app)

if __name__ == '__main__':
    importApp()
    exit(0)
