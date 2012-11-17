#!/usr/bin/env python
# encoding=utf8

import MySQLdb as DB
from data import App, RecApp

class BaseDbStorage(object):
    _host = 'localhost'
    _user = 'root'
    _password = '123456'
    _db = 'rec'

    _check_init_database_ = False

    def __init__(self):
        if not BaseDbStorage._check_init_database_:
            # create database
            self._execSQL('CREATE DATABASE IF NOT EXISTS %s' % self._db)
            BaseDbStorage._check_init_database_ = True
            # create tables
            self._execSQL(UserDbStorage._sql_create_table())
            self._execSQL(AppDbStorage._sql_create_table())
            self._execSQL(RecDbStorage._sql_create_table())
            self._execSQL(InstallDbStorage._sql_create_table())
            # create index
            self._execSQL('CREATE UNIQUE INDEX index_imei ON user(imei(16))')

    def _getConn(self):
        if self._check_init_database_:
            conn = DB.connect(self._host, self._user, self._password, self._db)
        else:
            conn = DB.connect(self._host, self._user, self._password)
        return conn

    @classmethod
    def _sql_create_table(clazz):
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (clazz._table, clazz._sql_columns_definition())

    def _value_to_sql(self, value):
        if isinstance(value, str):
            return "'%s'" % value
        return str(value)
        
    def _sql_insert(self, keys, values):
        return 'replace %s(%s) values(%s)' %(self._table, ','.join(keys), ','.join(map(self._value_to_sql, values)))

    @classmethod
    def _sql_columns_definition(clazz):
        sql = ''
        for col in clazz._columns:
            sql = sql + (' '.join(col) + ',')
        sql = sql  + ('primary key (%s)' % ','.join(clazz._primary_key))
        return sql

    def _insert(self, keys, values):
        self._execSQL(self._sql_insert(keys, values))

    def _execSQL(self, sql, closeAfter = True):
        conn = self._getConn()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print sql
        except:
            conn.rollback()
        finally:
            if closeAfter and conn:
                conn.close()
    
    def _querySql(self, sql):
        conn = self._getConn()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            print sql
            return cur.fetchall()
        finally:
            conn.close()


class UserDbStorage(BaseDbStorage):
    _table = 'user'
    _columns = (
        ('id', 'bigint unsigned', 'not null'),
        ('imei', 'varchar(128)', 'not null')
    )
    _primary_key = ('id',)

    def save(self, user):
        keys = ('id', 'imei')
        values = (user.id, user.imei)
        self._insert(keys, values)
    
    def getId(self, imei):
        results = self._querySql("SELECT id FROM %s WHERE imei='%s'" % (self._table, imei))
        if len(results) > 0:
            return results[0][0]
        else:
            return None

class RecDbStorage(BaseDbStorage):
    _table = 'recommend'
    _columns = (
        ('uid', 'bigint unsigned', 'not null'),
        ('aid', 'bigint unsigned', 'not null'),
        ('score', 'float', 'not null')
    )
    _primary_key = ('uid', 'aid')

    def save(self, rec):
        keys = ('uid', 'aid', 'score')
        values = (rec.uid, rec.aid, rec.score)
        self._insert(keys, values)

class InstallDbStorage(BaseDbStorage):
    _table = 'install'
    _columns = (
        ('uid', 'bigint unsigned', 'not null'),
        ('aid', 'bigint unsigned', 'not null'),
    )
    _primary_key = ('uid', 'aid')

    def save(self, install):
        keys = ('uid', 'aid')
        values = (install.uid, install.aid)
        self._insert(keys, values)

    def getAppIds(self, userId):
        sql = "SELECT aid FROM %s WHERE uid=%s" % (self._table, userId)
        results = self._querySql(sql)
        rList = []
        for row in results:
            rList.append(row[0])
        return rList

class AppDbStorage(BaseDbStorage):
    _table = 'app'
    _columns = (
        ('id', 'bigint unsigned', 'not null'),
        ('package', 'varchar(128)', 'not null'),
        ('name', 'varchar(128)', 'not null')
    )
    _primary_key = ('id',)

    def save(self, app):
        keys = ('id', 'package', 'name')
        values = (app.id, app.package, app.name)
        self._insert(keys, values)

    def getInstallApps(self, userId):
        sql = "SELECT a.id, a.package, a.name FROM app a LEFT JOIN install i ON a.id=i.aid WHERE i.uid = %s" \
            % userId
        results = self._querySql(sql)
        rList = []
        for row in results:
            id = row[0]
            package = row[1]
            name = row[2]
            rList.append(App(package, name, id))
        return rList

    def getRecommendApps(self, userId):
        sql = "SELECT a.id, a.package, a.name, r.score FROM app a LEFT JOIN recommend r ON a.id=r.aid WHERE r.uid = %s" \
            % userId
        results = self._querySql(sql)
        rList = []
        for row in results:
            id = row[0]
            package = row[1]
            name = row[2]
            score = row[3]
            app = App(package, name, id)
            recApp = RecApp(app, score)
            rList.append(recApp)
        return rList

if __name__ == '__main__':
    userStore = UserDbStorage()
    print userStore.getId('860984010484586')
