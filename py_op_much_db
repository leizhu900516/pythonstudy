import MySQLdb  #导入mysql
import redis    #导入redis
import happybase #导入hbase
一、操作mysql方式
1、不需要每次都close的操作方法
MYSQL_HOST= {'host':"192.168.8.176",'port':3306,'user':"chenhuachao",'passwd':'123'}
with contextlib.closing(MySQLdb.connect(**MYSQL_HOST)) as db:
    db.query("insert into test_blacklist.model (name,QQ,email) VALUES ('%s','%s','%s')"%(username,QQ,email))
    db.query("commit")

with MySQLdb.connect(host='172.17.16.50',port=3307,user='tj',passwd='jf(w#r82_MHf',db='server1',charset='utf8') as f:
    f.execute("select picurl from pd_info where cid = 300 and pid = 2244")
    result = f.fetchone()


2、需要每次都close的操作方法
conn= MySQLdb.connect(**MYSQL_HOST)
conn = MySQLdb.connect(**MYSQL_HOST)
cur = conn.cursor()
cur.execute("insert into test_blacklist.model (name,QQ,email) VALUES ('%s','%s','%s')"%(username,QQ,email))
cur.execute("select * FROM test_blacklist.model")
result = cur.fetchall()#获取查询的值
conn.commit()
cur.close()
二、操作redis方式
python连接redis
conn=redis.Redis(host='192.168.3.200',port=6380,db=0)
conn.zset('test','213')
查看redis磁盘空间
redis-cli -h 172.17.13.105 info|grep used_memory
三、操作hbase方式
hbase shell 进入命令行模式
list 列出所有的表
desc 'tables_name' 显示
conn=happybase.Connection('192.168.3.152')
table=conn.table("statistics")
row=table.row('T-G-ALL-201508')['DAY:11-UV']  #第一个'T-G-ALL-201508'是RowKey，第二个是cloumn-family1
print row
详细操作看http://happybase.readthedocs.org/en/l    atest/
四、操作mongodb
>>> import pymongo
>>> db=pymongo.MongoClient('localhost',27017)
>>> database = db.mydbs                            #连接mongodb的数据库mydbs
>>> database
Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'mydbs')
>>> collection = database.movice             #连接mydsb库中的movice表 
>>> collection.insert({"name":"zhangsan","age":45})          #插入数据
ObjectId('5747c0e35e38eb25edf120d4')
>>> collection.find_one({"name":"chenhuachao"})          #查询数据
{u'age': 12.0, u'_id': ObjectId('5747bf0351610d863032686a'), u'name': u'chenhuachao'}
>>> for i in collection.find():                       #批量查询
...     print i
... 
{u'age': 12.0, u'_id': ObjectId('5747bf0351610d863032686a'), u'name': u'chenhuachao'}
{u'age': 45, u'_id': ObjectId('5747c0e35e38eb25edf120d4'), u'name': u'zhangsan'}
{u'age': 45, u'_id': ObjectId('5747c5045e38eb25edf120d5'), u'name': u'zhangsanaa'}

