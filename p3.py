#coding = utf-8
import urllib
import re
import os


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    #print html
    return html

def mkDirAndDownloadImage(html):
	##modify
    reg = 'src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    name = getReportCode(html);
    fold = mkDirByName(name)
    x = 0
    for imgurl in imglist:
        ##print imgurl ##modify
        urllib.urlretrieve('http://baidu.com/'+imgurl, fold+'/image%s.jpg' % x)
        x+=1
    return imglist

def getReportCode(html):
	reg = '(\d{8}-\w*-?\w*)'
	codereg = re.compile(reg)
	foldname = re.findall(codereg, html)[0]
	return foldname

def mkDirByName(name):
	print 'mkDirByName:' + name
	##modify
	currentDir = 'C:/Users/wayli/Desktop/1111/'
	foldPath = currentDir + name
	if not os.path.exists(foldPath):
		os.mkdir(foldPath)
	return foldPath

def iterateFileNum(start, end):
	print 'getFileContent:' + str(start)+ '---' + str(end)
	##modify
	currentDir = 'C:/Users/wayli/Desktop/1111/'
	for index in range(start, end):
		current = currentDir + 'page' + str(index) +'.html'
		content = getFileContent(current)
		
		urls = getUrlsFromContent(content, index)
		print urls
		writeUrlsToText(urls, index)
		###detailUrls = readImageUrlText(index)
		for url in urls:
			html = getHtml('http://baidu.com/'+url)
			mkDirAndDownloadImage(html)
		#name = getReportCode(content)
		#fold = mkDirByName(name)

		writeDownLoadPageNum(index+1)


def getFileContent(path):
	print 'getFileContent:'+path
   	file_object = open(path)
	file_context = file_object.read() 
	file_object.close()
	return file_context

def getUrlsFromContent(content, index):
	print 'getUrlsFromContent:' + str(index)
	reg = '(patient_info.aspx\?id=\d*)'
	urlre = re.compile(reg)
	urls = list(set(re.findall(urlre, content)))
	return urls

def writeUrlsToText(urls, index):
	print 'writeUrlsToText:' + str(index)
	file_object = open('imageUrl' +str(index)+ '.text','w+');
	for url in urls:
		file_object.write(url + '\n') 
	file_object.close()

def readImageUrlText(index):
	print 'readImageUrlText:' + str(index)
	file_object = open('imageUrl' + str(index) + '.text','r');
	detailUrls = file_object.read().splitlines() 
	file_object.close()
	return detailUrls

def writeDownLoadPageNum(index):
	print 'writeDownLoadPageNum:page' + str(index)
	file_object = open('complete.log','w+')
	file_object.write(str(index))
	file_object.close()

def readDownLoadPageNum():
	print 'readDownLoadPageNum:'
	file_object = open('complete.log','a+')
	content = file_object.read().splitlines()
	file_object.close()
	print content[0]
	return int(content[0])

def init():
	start = readDownLoadPageNum()
	end = start + 500
	if (start == 1149):
		print 'complete download images'
		return 0
	if (end >= 1150):
		end = 1149
	print 'init' + str(start)+'---------' + str(end)
	iterateFileNum(start, end)

init()
#readDownLoadPageNum()

#html = getHtml("http://www.baidu.com")

#print getImg(html)