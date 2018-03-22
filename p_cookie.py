import urllib2 
import cookielib 
import urllib 
  
#第一步先给出账户密码网址准备模拟登录 
postdata = urllib.urlencode({ 
  'stuid': '1605122162', 
  'pwd': 'xxxxxxxxx'#密码这里就不泄漏啦，嘿嘿嘿 
}) 
loginUrl = 'http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp'# 登录教务系统的URL，成绩查询网址 
  
# 第二步模拟登陆并保存登录的cookie 
filename = 'cookie.txt'  #创建文本保存cookie 
mycookie = cookielib.MozillaCookieJar(filename) # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie)) #定义这个opener，对象是cookie 
result = opener.open(loginUrl, postdata) 
mycookie.save(ignore_discard=True, ignore_expires=True)# 保存cookie到cookie.txt中 
  
# 第三步利用cookie请求访问另一个网址，教务系统总址 
gradeUrl = 'http://ids.xidian.edu.cn/authserver/login?service'  #只要是帐号密码一样的网址就可以， 请求访问成绩查询网址 
result = opener.open(gradeUrl) 
print result.read()