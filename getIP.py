#自动获取最新的代理IP地址
import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_ip(html):

    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p,html)
   
    for each in iplist:
        print(each)
        
if __name__ == '__main__':
    url = "http://cn-proxy.com"
    get_ip(open_url(url))
