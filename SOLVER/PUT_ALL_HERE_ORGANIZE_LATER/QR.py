'''
Pings an image online and one locally
xors the image bruteforcing the encoding scheme used
'''

import requests
from PIL import Image
import base64
import os
import sys
from bs4 import BeautifulSoup
import time
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

orig = Image.open("hex.png")
orig_w, orig_h = orig.size
orig_p = orig.convert("RGB")

def xor(im):
    c = 0
    width,height = im.size
    imp = im.convert("RGB")
    for x in range(width):
        for y in range(height):
            pix1 = orig_p.getpixel((x,y))
            if (pix1 == (255, 255, 255)):
                pix1 = 1
            else:
                pix1 = 0
            pix2 = imp.getpixel((x,y))
            if (pix2 == (255, 255, 255)):
                pix2 = 1
            else:
                pix2 = 0
            if(pix1 ^ pix2 == 0):
                c += 1
    return c

def extract(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        gu = (soup.find('img')['src'])
        return (gu[gu.find("base64,") + 7:])
    except:
        return "bad!"

str1 = list("a" * 57)
for i in range (57):
    cnt = -1
    ascii = "a"
    for j in "abcdefghijklmnopqrstuvwxyz_{}?!":
        blah = str1
        blah[i] = j
        g = open("test.png", "wb")
        print(''.join(blah))
        r = requests.post("http://hexqr.web.easyctf.com/", data={'text': ''.join(blah)})
        res = extract(r.text)
        if(res == "bad!"):
            print("bad!")
        else:
            g.write(base64.b64decode(extract(r.text)))
            g.close()
            gu = Image.open("test.png")
            anr = xor(gu)
            print (anr)
            if(anr == cnt):
                print("problem")
            if (anr > cnt):
                cnt = anr
                ascii = j
        os.remove("test.png")
        time.sleep(0.75)
    str1[i] = ascii
    print("".join(str1))