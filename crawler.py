# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8') 

pchinese=re.compile(ur'([\u4e00-\u9fa5]+)+?', re.U)
pch = re.compile(u'[\u4e00-\u9fa5]+', re.U)

fw = open('romantic.txt', 'w')

list = []
for i in range(0,50):
	#crawler.py运行三次，分别取消注释
	req = urllib2.Request('http://movie.douban.com/tag/爱情?start='+ str(i*20) +'&type=T')
	#req = urllib2.Request('http://movie.douban.com/tag/悬疑?start='+ str(i*20) +'&type=T')
	#req = urllib2.Request('http://movie.douban.com/tag/科幻?start='+ str(i*20) +'&type=T')
	webpage = urllib2.urlopen(req)
	s = webpage.read() 

	soup = BeautifulSoup(s)
	for item in soup.findAll(name="a", attrs={"class":"", "href":re.compile(r"movie.douban.com/subject(\s\w+)?")}):
		movieTitle = item.contents[0].strip().strip('/').strip()+'\n'
		print movieTitle
		list.append(movieTitle)
		fw.write(movieTitle)

fw.close()
