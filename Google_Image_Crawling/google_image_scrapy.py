##lazyerIJ
##Google_Image_Scrapy_v0.1
##python 3.6.5
##bs4 4.6.0

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import datetime

def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
def scrapy_image():
    while(True):
        #exit scrapy
        print("TARGET (type 'qq' to exit)>>>")
        find_target = input()
        if find_target=='qq':
            break
        data = {}
        
        #basic url
        req = requests.get('https://www.google.co.kr/search?newwindow=1&biw=725&bih=910&tbm=isch&sa=1&q='+find_target,
                 headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        my_titles = soup.select('div > a > img')

        if not os.path.isdir(find_target):
            os.mkdir(find_target)
        os.chdir(os.getcwd()+'/'+find_target)

        for step, title in enumerate(my_titles):
            data[title.text] = title.get('data-src')
            try:
                #fname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+str(step + 1)
                fname = '{}_{}'.format(find_target, str(step+1))
                #urllib.request.urlretrieve(title.get('src'),str(step) +".jpg")
                urllib.request.urlretrieve(data[title.text],fname +".jpg")
                #print(data[title.text])
            except:
                #print("pass")
                pass
        print('\n\n')

if __name__ == '__main__':
    #check directory
    #loc of directory to save image
    img_dir = 'data'
    working_dir = os.path.join(os.getcwd(), img_dir)
    make_dir(working_dir)
    os.chdir(working_dir)
    scrapy_image()
