# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

pchinese=re.compile(ur'([\u4e00-\u9fa5]+)+?', re.U)

#scratcher.py运行三次，分别取消注释
f = open("science.txt", "r")
#f = open("romantic.txt", "r")
#f = open("suspense.txt", "r")

movieTitleList = list()
for line in f:
	movieTitleList.append(line)

#scratcher.py运行三次，分别取消注释
fw = open("scienceResult", "w")
#fw = open("romanticResult", "w")
#fw = open("suspenseResult", "w")

#对于电影title列表文件中每个电影条目
#访问其百科页面，抽取其中的div.para HTML DOM内容
for movieTitle in movieTitleList:
	#Use redirect link to access the webpage
	urlString = "http://baike.baidu.com/searchword/?word="
	urlString += movieTitle.strip()
	urlString += "&pic=1&sug=1&enc=utf-8"
	print "MOVIETITLE", movieTitle.strip()

	#Get Access to the page
	req = urllib2.Request(urlString)
	req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
	webpage = urllib2.urlopen(req)
	s = webpage.read()

	soup = BeautifulSoup(s)

	#使用BeautifulSoup抽取相应的HTML DOM
	allDivPara = soup.findAll(name="div", attrs={"class":"para"})
	if allDivPara == []:
		#验证码页面里面不会有div.para
		print "Could not visit the baike page!"
	else:
		print "OK"

	#对于每个条目，写入结果文档
	for item in allDivPara:
		string = str(item)
		line = pchinese.findall(string.decode('utf-8'))
		for it in line:
			fw.write(it.encode('utf-8'))

fw.close()