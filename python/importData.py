#!/usr/bin/env python
# encoding=utf8

import codecs
from data import App, User, Rec, Install
import utils, IdUtils
from dbStorage import AppDbStorage, UserDbStorage, RecDbStorage, InstallDbStorage

appStore = AppDbStorage()
userStore = UserDbStorage()
recStore = RecDbStorage()
installStore = InstallDbStorage()

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

def importOthers():
    input = codecs.open('../data/rec.data', 'r', 'gbk');

    users = {}
    recs = {}
    installs = {}
    count = 0
    for line in input.readlines():
        count = count + 1
        print 'count=',count
        line = line.encode('utf8')
        l = line.split('|', 3)
        imei = l[0]
        if imei not in users:
            users[imei] = User(imei)

        packages = set()
        for ll in l[1].split(','):
            package = ll.split('\t')[0]
            packages.add(package)
        installs[imei] = packages

        recApps = []
        for ll in l[2].split(','):
            lll = ll.split()
            if len(lll) > 0:
                package = lll[0]
                score = float(lll[1])
                recApps.append((package, score))
        recs[imei] = recApps

        if count == 100:
            break

    for imei in users:
        userStore.save(users[imei])

    for imei in installs:
        packages = installs[imei]
        user = users[imei]
        for package in packages:
            aid = IdUtils.genId(package)
            installStore.save(Install(user.id, aid))
    for imei in recs:
        recApps = recs[imei]
        for rec in recApps:
            aid = IdUtils.genId(rec[0])
            score = rec[1]
            uid = users[imei].id
            recStore.save(Rec(uid, aid, score))

if __name__ == '__main__':
    importApp();
    importOthers()
    exit(0)
