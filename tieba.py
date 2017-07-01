#百度贴吧某帖中的图片下载
import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    #正则表达式".*?"表示元字符"."重复匹配零次到多次，"?"表示对表示重复的元字符"*"启用飞贪婪模式，即在遇到第一个src的时候就停下来
    #正则表达式'[^"]'表示匹配非双引号'"'字符'+'表示匹配一次到多次
    p = r'<img class="BDE_Image".*?src="([^"]+\.jpg)'
    imglist = re.findall(p,html)
    '''
    for each in imglist:
        print(each)
    '''
    for each in imglist:
        #split("/")表示按反斜杠"/"分割，获得一个字符串列表，然后将最后一个元素赋值filename
        filename = each.split("/")[-1]
        #urlretrieve函数表示将将each网址保存到filename路径，none 参数表示下载速度
        urllib.request.urlretrieve(each,filename,None)
        
if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/5193055422"
    get_img(open_url(url))
