#!/usr/bin/python

import os
import sys
import re
import urllib2

url = "https://www.yahoo.co.jp"
title = "page2"
img_tag = []
img_url = []
img_path = os.getcwd()

pat_title = re.compile('<title>(.*?)</title>')
pat_a1 = re.compile('<a[\s]*href[\s]*=.*?>')
pat_a2 = re.compile('href[\s]*="(.*?)"')
pat_img1 = re.compile('<img[\s]*src[\s]*=.*?>')
pat_img2 = re.compile('src[\s]*="(.*?)"')
pat_img3 = re.compile('.+/(.*)')
img_format = [".jpg", ".png", ".gif", ".bmp"]

#def image_download(url, output):
#    opener = urllib2.build_opener()
#    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
#    img_file = open(output, 'wb')
#    
#    img_file.write(opener.open(req).read())
#    img_file.close()

def image_download(url, output):
    link = urllib2.Request(url)
    try:
        response = urllib2.urlopen(link)
        out = open(output, 'wb')
        out.write(response.read())
        out.close()
    except ValueError:
        pass

if __name__ == "__main__":
    req = urllib2.Request(url, headers={'user-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)
    html = con.read()

    m = pat_title.search(html)
    title1 = m.group(1)
    dl_path = img_path + "/" + title
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    os.chmod(img_path, 0777)
    os.chmod(dl_path, 0777)

    a_tag = pat_a1.findall(html)
#    print a_tag
    img_tag = pat_img1.findall(html)
#    print img_tag
    for i in a_tag:
        m = pat_a2.search(i)
        if not m is None:
            tmp = m.group(1)
#            print tmp
            for j in img_format:
                if tmp.find(j) > -1:
                    img_url.append(tmp)
                    break
#    print img_url
    for i in img_tag:
        m = pat_img2.search(i)

        if not m is None:
            tmp = m.group(1)

            for j in img_format:
                if tmp.find(j) > -1:
                    img_url.append(tmp)
                    break

    for i in img_url:
        m = pat_img3.search(i)
        print m
        name = m.group(1)
        output = dl_path + "/" + name
        image_download(i, output)


