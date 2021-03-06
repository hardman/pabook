#coding=utf-8

import pymysql
import pymysql.cursors

from src.utils import Utils, Log

from Config import Config

class Db:
    #pymysql接口
    def __init__(self):
        Log.D("[I] init class Db");
        connConfig = {
            'host': '127.0.0.1',
            'user': Config.shared.dbUser,
            'password': Config.shared.dbPwd,
            'db': Config.shared.dbName,
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
            'autocommit': True
        };
        self.conn = pymysql.connect(**connConfig);
        self.cursor = self.conn.cursor();

    def executeSql(self, sql):
        try:
            self.cursor.execute(sql);
            Log.I("[I] 执行 " + sql.strip() + " 成功");
            return True; 
        except Exception as e:
            if not isinstance(e, pymysql.err.IntegrityError) or len(e.args) <= 0 or e.args[0] != 1062:
                Log.E("[I] 执行 " + sql.strip() + " 失败");
                Log.Exc(e);
        return False;

    def fetchOne(self):
        return self.cursor.fetchone();

    def fetchAll(self):
        return self.cursor.fetchall();

    def __del__(self):
        Log.D("[I] class Db dealloc");
        self.conn.close();

instance = Db();

