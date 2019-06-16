from __future__ import print_function
import urllib.request
import urllib.parse
import os
import random
from urllib.error import URLError
from PIL import Image
import platform
from bs4 import BeautifulSoup

def hdrgen():
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)'
        ' Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET'
        ' CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5'
        ' (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731'
        'Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko)'
        ' Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77'
        'Safari/535.7',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101'
        'Firefox/10.0 ', ]
    agent = random.choice(user_agents)
    hdr = {
        'User-agent': agent,
        'Accept': 'text/home_html,application/xhtml+xml,\
            application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    return hdr


def getHtml(url):
    hdr = hdrgen()
    req = urllib.request.Request(url, None, hdr)
    page = urllib.request.urlopen(req)
    home_html = page.read()
    return home_html


root_url = 'https://qingbuyaohaixiu.com'
pwd = os.getcwd()
# 修改 start_page 和 end_page 来确定想要获取的相册范围。
start_page = 4
end_page = 10
for i in range(start_page, end_page + 1):
    pagenum = str(i)
    pageurl = root_url+'?page='+pagenum
    home_html = getHtml(pageurl)
    home_soup = BeautifulSoup(home_html, \\\"html.parser\\\")
    pics = home_soup.findAll(\\\"div\\\", {\\\"class\\\": \\\"rcm4\\\"})

    for pic in pics:
        alburl = root_url + pic.contents[5].attrs['href']
        print(alburl)
        alb_html = getHtml(alburl)
        alb_soup = BeautifulSoup(alb_html, \\\"html.parser\\\")
        imgs = alb_soup.findAll(\\\"div\\\", {\\\"class\\\": \\\"rcx12 rcm9 rcl9\\\"})

        if platform.system() == 'Darwin':
            imagedir = pwd + '/image'
            if not os.path.exists(imagedir):
                os.makedirs(imagedir)
            jpgdir = imagedir + '//' + 'Page' + pagenum
            print(jpgdir)
        elif platform.system() == 'Windows':
            imagedir = pwd + '\\' + 'image'
            if not os.path.exists(imagedir):
                os.makedirs(imagedir)
            jpgdir = imagedir + '\\' + 'Page' + pagenum

        if not os.path.exists(jpgdir):
            os.makedirs(jpgdir)
        os.chdir(jpgdir)

        imgurl = imgs[0].contents[7].attrs['src']
        imgname = imgs[0].contents[1].contents[0]
        print(imgurl)

        hdr = hdrgen()
        req = urllib.request.Request(imgurl, None, hdr)

        try:
            response = urllib.request.urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
        else:
            tmp = 'test'
            output = open('%s.webp' % tmp, 'wb')
            output.write(response.read())
            output.close()
            im = Image.open('%s.webp' % tmp).convert(\\\"RGB\\\")
            im.save(imgname+\\\".jpg\\\", \\\"jpeg\\\")
            im.close()
            os.remove(tmp+\\\".webp\\\")
            print(str(pics.index(pic)) + ' Finished')