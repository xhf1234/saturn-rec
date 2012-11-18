#!/usr/bin/env python

from store import AppStore, UserStore
from data import User, App, RecApp
import utils
import random

appStore = AppStore()
userStore = UserStore()

class BaseService(object):
    pass

class AppService(BaseService):
    def getRecommendApps(self, imei):
        user = User(imei)
        return appStore.getRecommendApps(user.id)

    def getInstallApps(self, imei):
        user = User(imei)
        return appStore.getInstallApps(user.id)

class UserService(BaseService):
    def getRandomUsers(self, count):
        total = userStore.count()
        rdm = random.randint(0, total-count-1)
        return userStore.getUsers(rdm, count)

if __name__ == '__main__':
    appService = AppService()
    userService = UserService()
    users = userService.getRandomUsers(10)
    print utils.listToJson(users)
