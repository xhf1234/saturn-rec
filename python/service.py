#!/usr/bin/env python

from store import AppStore
from data import User, App, RecApp
import utils

appStore = AppStore()

class BaseService(object):
    pass

class AppService(BaseService):
    def getRecommendApps(self, imei):
        user = User(imei)
        return appStore.getRecommendApps(user.id)

    def getInstallApps(self, imei):
        user = User(imei)
        return appStore.getInstallApps(user.id)

if __name__ == '__main__':
    appService = AppService()
    apps = appService.getRecommendApps('860984010484586')
    print utils.listToJson(apps)
