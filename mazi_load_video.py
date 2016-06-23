# coding:utf-8
__author__ = 'chenhuachao'
# --------------------------------
# Created by chenhuachao  on 201x/xx/xx.
# ---------------------------------
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import urllib2
import re
import urllib
from bs4 import BeautifulSoup
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数,用于显示下载进度的
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent


def download():
    '''下载麦子学院的python视频，第二版'''
    n=0
    url_list = []
    url = "http://www.maiziedu.com/course/543-7437/"
    result = urllib2.urlopen(url).read()
    source = BeautifulSoup(result,"html5lib")
    div_tag = source.find_all('div',attrs={"class":"playlist scroll-pane"})
    li_source = BeautifulSoup(str(div_tag),"html5lib")
    li_tag = li_source.find_all('a')
    for link in li_tag:
        url_list.append("http://www.maiziedu.com"+link.get('href'))
    print url_list
    for url  in url_list:
        result = urllib2.urlopen(url).read()
        name = BeautifulSoup(result,"html5lib").find_all('span',attrs={"class":"col_l"})
        # print name
        down_address = BeautifulSoup(result,"html5lib").find_all("source")
        print "{0}.mp4".format([link.get_text() for link in name if link][n])
        urllib.urlretrieve([link.get('src') for link in down_address if link][0],"{0}.mp4".format([link.get_text() for link in name if link][n]).decode(),callbackfunc)
        n+=1
        print "{0}已经下载完成url={1}".format([link.get_text() for link in name if link][0],url)
if __name__ =="__main__":

    download()
