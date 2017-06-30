#从煎蛋网爬妹子图的代码，待改善
import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')

    #使用代理后程序运行不会结束也没有结果
    #proxies = ['61.176.215.7:8080','124.42.7.103:80','182.92.81.200:8081','182.254.222.45:80']
    #proxy = random.choice(proxies)

    #proxy_support = urllib.request.ProxyHandler({'http':proxy})
    #opener = urllib.request.build_opener(proxy_support)
    #urllib.request.install_opener(opener)
    
    response = urllib.request.urlopen(req)
    
    html = response.read()

    print(url)
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23      #find函数如果查到：返回查找的第一个出现的位置。否则，返回-1
    b = html.find(']',a)                            #从a开始查找']'

    return html[a:b]                                #html[a:b]是从字符串中a的位置（包括a）到b的位置（不包括b）切片创建新列表

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')                           #查找图片网址前面的字符串

    while a != -1:
        b = html.find('.jpg',a,a+225)                   
        if b != -1:
            img_addrs.append('http:' + html[a+9:b+4])   #从html的字符串中切片得到图片网址，从网页检查发现返回的html对象里面的图片网址缺少'http:'，故手动加上
        else:
            b = a + 9

        a = html.find('img src=',b)

        return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            

def download_mm(folder='ooxx',pages=100):               #查找100次 ，手动输入次数，以后可修改代码实现运行中输入
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()

    
