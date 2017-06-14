import os
import urllib2, urllib
from bs4 import BeautifulSoup

url = "https://www.yahoo.co.jp"
outputFolder = "yahooGazou"

if __name__ == '__main__':
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    html = urllib2.urlopen( req )
#    print html.read()

    soup = BeautifulSoup(html, "html.parser")
#    print soup
    srcTagList = soup.findAll(src=True)

#    print srcTagList

    for srcTag in srcTagList:
        srcUrl = srcTag["src"]

        if srcUrl is not None:
            #print srcUrl
            root, ext = os.path.splitext(srcUrl)
            if ext in ['.jpg', '.jpeg', '.png', 'gif']:
                #print root
                filePath = outputFolder + '/' + os.path.basename(srcUrl)
                #print filePath
                if not os.path.exists(outputFolder):
                    os.makedirs(outputFolder)
                urllib.urlretrieve(srcUrl, filePath)
