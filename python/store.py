#!/usr/bin/env python

from dbStorage import UserDbStorage, AppDbStorage, RecDbStorage, InstallDbStorage
from structure import FIFOCache
from data import User, App
import utils

userDb = UserDbStorage()
installDb = InstallDbStorage()
appDb = AppDbStorage()

class BaseStore(object):
    pass

class AppStore(BaseStore):
    def getInstallApps(self, userId):
        return appDb.getInstallApps(userId)
    
    def getRecommendApps(self, userId):
        return appDb.getRecommendApps(userId)
        

class UserStore(BaseStore):
    
    _idCache = FIFOCache()
    _countCache = None
    
    def getUserByImei(self, imei):
        user = self._idCache.get(imei)
        if user is None:
            userId = userDb.getId(imei)
            user = User(imei, userId)
            self._idCache.put(imei, user)
        return user
    
    def count(self):
        if self._countCache is None:
            self._countCache = userDb.count()
        return self._countCache
    
    def getUsers(self, offset, limit):
        return userDb.getUsers(offset, limit)

if __name__ == '__main__':
    appStore = AppStore()
    userStore = UserStore()
    print userStore.count()
