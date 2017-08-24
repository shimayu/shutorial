from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
import os

def findImgLink(bsObj):
    for link in bsObj.findAll("a"):
        img_link = link.find("img")
        if img_link is not None:
            src = img_link.attrs['src']
            srcList.add(src)
            # print(src)

def downloadImg(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for src in srcList:
        img_name = urlparse(src).path
        img_name = img_name.replace("/", "")
        # print(img_name)
        dpath = dirname + "/" + img_name
        # print(dpath)
        urlretrieve(src, dpath)


def main():
    try:
        html = urlopen("http://www.pythonscraping.com")
        bsObj = BeautifulSoup(html, "html.parser")
    except URLError as e:
        print(e)
        return
    except HTTPError as e:
        print(e)
        return
    dirname = "ImgDownload"
    findImgLink(bsObj)
    downloadImg(dirname)

if __name__=='__main__':
    srcList = set()
    main()    
        
