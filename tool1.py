import urllib.request
import chardet
def main():
    url = input('请输入网址：')
    if url[:7] != 'http://':
        url = 'http://' + url

    reponse = urllib.request.urlopen(url)
    html = reponse.read()

    encode = chardet.detect(html)['encoding']       #需要安装chardet库，
    if encode == 'GB2312':
        encode = 'GBK'

    print('该网页使用的编码是：%s'%encode)

if __name__ == '__main__':
    main()
