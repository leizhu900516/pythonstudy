#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import SocketServer
import json, types,string
import os, time
from gcutils.queue import KafkaMgr
import logging
import datetime
hosts="192.168.3.1:9092,192.168.3.2:9092"
topic='statis-baseinfo-serverevent'
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        start_time=time.time()
        print start_time
        data = self.request.recv(2048)
        jdata = json.loads(data)
        print type(jdata)
        log = logger("socket_logging")
        print jdata['data'],jdata['event']
        # if not jdata['data'] or jdata['event']:
        #     logger("socket_logging")
        try:
            assert jdata['data']!=""
            assert jdata['event']!=""
        except Exception as e:
            log.info(data,e.message)
        else:
            msg = {"status":True}
            log.info(data,msg)
        try:
            kafka=KafkaMgr(hosts)
            kafka.send_message(topic,data)
        except Exception as e:
            pass
        #     msg=e.message
        # else:
        #     msg='success'
        if data:
            msg = json.dumps({"status":True})
            self.request.sendall(msg)
        elif not data:
            msg = json.dumps({"status":False})
            self.request.sendall(msg)

        print self.client_address
        print "recv:",jdata
        # host=self.client_address
        # sub_thread = threading.current_thread()
        # response = {'data':data,'message':msg}
        # print response
        # jresp = json.dumps(response)
        # self.request.sendall(jresp)
        print 'count_time---',time.time()-start_time

def logger(user_name):
    "日志功能模块"
    logger = logging.getLogger(user_name)
    logger.setLevel(logging.CRITICAL)
    log_file = '/tmp/tj/tj'
    if not os.path.exists('/tmp/tj'):
        os.makedirs('/tmp/tj')
    del_day = (datetime.datetime.now()+datetime.timedelta(days=-3)).strftime("%Y%m%d")
    # last_mouth = int(time.strftime("%Y%m",time.localtime())) - 1
    fn=logging.FileHandler(log_file+'_'+user_name+'_'+time.strftime("%Y%m%d",time.localtime())+'.log')
    fn.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    fn.setFormatter(formatter)
    #cn =logging.StreamHandler()#用于输出异常到屏幕，用到时开启
    #cn.setLevel(logging.DEBUG)
    #cn.setFormatter(formatter)
    #logger.addHandler(cn)
    logger.addHandler(fn)
    # try:
    #     os.system('rm -rf %s_%s_%s.log'%(log_file,user_name,del_day))#删除前3天的日志文件
    #     # os.system('rm -rf %s_%s_%s*'%(log_file,user_name,last_mouth))#删除前一月的日志文件
    # except:
    #     pass
    return logger

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    # SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.ThreadingTCPServer(('192.168.12.189',50001), ThreadedTCPRequestHandler)
    # ip, port = server.server_address
    # home_thread = threading.Thread(target=server.serve_forever)
    # home_thread.start()
    # print "Server loop running in thread:", home_thread.name
    print " .... waiting for connection"
    server.serve_forever()

