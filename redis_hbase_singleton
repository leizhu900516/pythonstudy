# coding:utf-8
__author__ = 'chenhuachao'
# --------------------------------
# Created by chenhuachao  on 201x/xx/xx.
# ---------------------------------
'''
python实现redis和hbase的单例模式
'''
import happybase
import redis
class _RedisMgrSingleton(type):
    '''redis的单例'''
    def __init__(self, name, bases, dict):
        super(_RedisMgrSingleton, self).__init__(name, bases, dict)
        self._instance = {}
    def __call__(self, host,port,db):
        if not self._instance.has_key((host,port,db)):
            self._instance[(host,port,db)] = super(_RedisMgrSingleton, self).__call__(host,port,db)
        return self._instance[(host,port,db )]

class HbaseSingleton(type):
    '''hbase的单例'''
    def __init__(self, name, bases, dict):
        super(HbaseSingleton, self).__init__(name, bases, dict)
        self._instance = {}
    def __call__(self, host,table):
        if not self._instance.has_key((host,table)):
            self._instance[(host,table)] = super(HbaseSingleton, self).__call__(host,table)
        return self._instance[(host,table)]

class RedisMgr:
    "redis操作专用类"
    def  __init__(self,host,port,db,max_connections=3):
        "eg:  host    '192.168.2.184'   port  6379    db   14"
        self.host=host
        self.port=port
        self.db=db
        self.conn=redis.Redis(connection_pool= redis.ConnectionPool(host=host,port=port,db=db,max_connections=max_connections))
    def run_redis_fun(self,funname,*args):
        fun=getattr(self.conn,funname)
        print args
        return  fun(*args)
    def pipe(self):
        return self.conn.pipeline(transaction=False)
    __metaclass__ = _RedisMgrSingleton      #元类实现单例



class HbaseOperate(object):
    def __init__(self,host,table):
        self.host = host
        self.table = table
        self.conn = happybase.Connection(self.host)
        self.table = self.conn.table(self.table)

    def run(self,fun,*args):
        # result =self.table.row(*args)
        funname = getattr(self.table,fun)
        return funname(*args)
    def cells(self,column,info,version):
        return self.table.cells(column,info,versions=version)
    __metaclass__ = HbaseSingleton      #元类实现单例



conn = HbaseOperate('xxx.xx.11.8',"history_visitor_product")
result = conn.cells('chenhuachao','info:visiotr',3)
print result
print "第一次",id(conn)
conn1 = HbaseOperate('xxx.xxx.11.8',"history_visitor_product")
result1= conn1.cells('chenhuachao','info:visiotr',6)
print result1
print "第二次",id(conn1)

