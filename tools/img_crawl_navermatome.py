from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
import os
import re

def getFirstLinks(url):
    FirstLinks = []
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
    except URLError as e:
        print(e)
        return
    except HTTPError as e:
        print(e)
        return
    except AttributeError as e:
        return

    for link in bsObj.findAll("a",
            href=re.compile("^(/odai/2130012623348707001/).*")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in FirstLinks:
                FirstLinks.append(link.attrs['href'])
    return FirstLinks


def getLinks(url):
    ImgLinks = []
    try:
        html = urlopen("https://matome.naver.jp" + url)
        bsObj = BeautifulSoup(html, "html.parser")
    except URLError as e:
        print(e)
        return
    except HTTPError as e:
        print(e)
        return
    except AttributeError as e:
        return

    for link in bsObj.findAll("a", 
            href=re.compile(".*\.jpg$")):
        srcList.add(link.attrs['href'])
        

#def getImgLinks(url):
#    try:
#        html = urlopen(url)
#        bsObj = BeautifulSoup(html, "html.parser")
#    except URLError as e:
#        print(e)
#        return
#    except HTTPError as e:
#        print(e)
#        return
#    except AttributeError as e:
#        return
#
#    img_link = bsObj.find("img")
#    if img_link is not None:
#        print(img_link)
#        src = img_link.attrs['src']
#        #srcList.add(src)
#        print(src)


def downloadImg(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for src in srcList:
        #print(src)
        img_name = urlparse(src).path
        img_name = img_name.replace("/", "")
        #print(img_name)
        dpath = dirname + "/" + img_name
        #print(dpath)
        urlretrieve(src, dpath)


def main():
    url = "https://matome.naver.jp/odai/2130012623348707001"
    dirname = "NanohaDownload"
    urlLinks = getFirstLinks(url)
    imgLinks = []
    for i in range(len(urlLinks)):
        getLinks(urlLinks[i])
        
    downloadImg(dirname)

if __name__=='__main__':
    srcList = set()
    main()    
        
