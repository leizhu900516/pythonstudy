#coding=utf-8
__author__ = 'chenhuachao'
# --------------------------------
# Created by chenhuachao  on 2015/7/7.
# ---------------------------------
#rabbitmq队列的消费者模式
 
from pika import  connection,BlockingConnection,ConnectionParameters,credentials,BasicProperties
import  time
def get_rmq_channel(host,port,user,passwd):
    "获取连接到rabbitmq的通道对象"
    conn=BlockingConnection(ConnectionParameters(host=host,port=port,credentials=credentials.PlainCredentials(username=user,password=passwd)))
    return  conn.channel()
 
channel.queue_declare(queue='statis_cateid_redis_test')#进入需要取数据的队列
print "waiting for n"
 
def request(ch,method,properties,body): #定义一个回调函数，用来取数据
        print "increase(%s)"%(body,)
conn=get_rmq_channel(host="192.168.3.156",port=5672,user="xxx",passwd="xxx")
conn.basic_consume(request,queue="statis_cateid_redis_test")
conn.start_consuming()
