import urllib.request
import random

#获取本机ip地址的网址：www.whatismyip.com.tw
url = 'http://www.whatismyip.com.tw'

#获取代理ip网址：cn-proxy.com
iplist = ['61.130.97.212:8099','182.254.222.45:80','1.82.132.75:8080']          

#创建opener
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)

#定制opener
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]

#安装opener到系统
urllib.request.install_opener(opener)

#获取服务器响应的response对象，url参数可以是字符串或者Request对象
response = urllib.request.urlopen(url)

#将Request对象传给urlopen函数，返回一个类文件对象，用read方法来读取内容
html = response.read().decode('utf-8')

print(html)
