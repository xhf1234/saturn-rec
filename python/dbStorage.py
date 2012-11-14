#!/usr/bin/env python
# encoding=utf8

import MySQLdb as DB

class BaseDbStorage(object):
    _host = 'localhost'
    _user = 'root'
    _password = '123456'
    _db = 'rec'

    def __init__(self, ):
        self._createTableIfNotExists()

    def _getConn(self):
        conn = DB.connect(self._host, self._user, self._password, self._db)
        return conn

    def _createTableIfNotExists(self):
        self._execSQL(self._sql_create_table());

    def _sql_create_table(self):
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (self._table, self._sql_columns_definition())

    def _value_to_sql(self, value):
        if isinstance(value, str):
            return "'%s'" % value
        return str(value)
        
    def _sql_insert(self, keys, values):
        return 'replace %s(%s) values(%s)' %(self._table, ','.join(keys), ','.join(map(self._value_to_sql, values)))

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

class AppDbStorage(BaseDbStorage):
    _table = 'app'
    _columns = (
        ('id', 'bigint unsigned', 'not null'),
        ('package', 'varchar(128)', 'not null'),
        ('name', 'varchar(128)', 'not null')
    )
    _primary_key = ('id',)

    def _sql_columns_definition(self):
        sql = ''
        for col in self._columns:
            sql = sql + (' '.join(col) + ',')
        sql = sql  + ('primary key (%s)' % ','.join(self._primary_key))
        return sql

    def save(self, app):
        keys = ('id', 'package', 'name')
        values = (app.id, app.package, app.name)
        self._insert(keys, values)

if __name__ == '__main__':
    AppDbStorage()
