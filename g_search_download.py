from bs4 import BeautifulSoup
import requests
import os
import re
import time
from tqdm import tqdm

# put here your keywords for search
keywords = []

class GoogleeImageDownloader(object):
    _URL = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch"
    _BASE_DIR = 'titles_dir'
    _HEADERS = {
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    def __init__(self, query):
        self.query = query
        self.dir_name = os.path.join(self._BASE_DIR, query.split()[0])
        self.url = self._URL.format(query) 
        self.make_dir_for_downloads()
        self.initiate_downloads()

    def make_dir_for_downloads(self):
        print("Creating necessary directories")
        if not os.path.exists(self._BASE_DIR):
            os.mkdir(self._BASE_DIR)

        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)

    def initiate_downloads(self):
        src_list = []
        soup = BeautifulSoup(requests.get(self.url).text,'html.parser')
        for i in soup.find_all('a'):
            try:
                src_list.append(re.search(r'.*src="(.*)".*', str(i)).group(1))
            except:
                pass
        
        print("{} of images collected for downloads".format(len(src_list)))
        self.save_images(src_list)

    def save_images(self, src_list):
        print("Saving Images...")
        for i , src in enumerate(src_list):
            try:
                req = requests.get(src, headers=self._HEADERS)
                with open(os.path.join(self.dir_name , str(i)+".jpg"), 'wb') as f:
                    f.write(req.content)
            except Exception as e:
                print ("could not save image")
                pass


if __name__ == "__main__":
    for kw in tqdm(keywords, position=0, leave=True):
        GoogleeImageDownloader(kw)
        time.sleep(3)