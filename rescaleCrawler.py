#imports!
import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests
import validators
  
  
class threadedCrawler:
  
    def __init__(self, initURL, maxDepth):
        #initial url
        self.initURL = initURL

        #pool of workers (changeable)
        self.pool = ThreadPoolExecutor(max_workers=4)

        #keep track of what pages have been crawled
        self.cache = set()

        #Queue of links to crawl, starting with initial url
        self.crawl_queue = Queue()
        self.crawl_queue.put(self.initURL)

        #options for controlling depth of crawl
        self.currentDepth = 0
        self.maxDepth=maxDepth
        self.linksSeen=0
  
    def recursiveCrawl(self, res):
        #check if status code is good and results are there
        result=res.result()
        if result and result.status_code == 200:
            html=result.text
            url=result.url
        else:
            return

        #using bs4 to parse out html and find all links on the page
        soup = BeautifulSoup(html, 'html.parser')
        subLinks = soup.find_all('a', href=True)

        #use validSubLinks to keep track of the links we will crawl
        validsubLinks = []

        #print the url we are crawling for the requested logging structure
        print(url)

        #go through the sublinks
        for link in subLinks:
            url = link['href']

            #if it's valid, print it then add to the list of validSubLinks
            #we print out all the valid ones before the start crawling any of
            #them in order to acheive our requested logging structure

            #use validators library to check if url is absolute
            if validators.url(url):
                print('   ',url)
                if url not in self.cache:
                    validsubLinks.append(url)

        #crawl them all!
        for url in validsubLinks:
            self.crawl_queue.put(url)

        #increase our depth
        self.currentDepth+=1
  
    def checkLink(self, url):
        #get url info/check if returning anything
        try:
            res = requests.get(url, timeout=(10))
            return res
        except:
            return
  
    def crawl(self):
        while True:
            try:
                #grab the next url and/or wait 30 seconds to see if any get queued 
                try:
                    queuedURL = self.crawl_queue.get(timeout=30)
                    self.linksSeen+=1
                #if the queue is empty, we are done
                except Empty:
                    return

                #check if we've crawled it yet
                if queuedURL not in self.cache:
                    #break loop if max depth is reached
                    if self.currentDepth >= self.maxDepth:
                        return
                    #add it to cache so that we don't recrawl it
                    self.cache.add(queuedURL)

                    #start a thread for the url, if it returns something
                    #go crawl it!
                    thread = self.pool.submit(self.checkLink, queuedURL)
                    thread.add_done_callback(self.recursiveCrawl)
                    
            #if link doesn't work, just go to the next
            except Exception as e:
                print('Error at ',targer_url,': ',e)
                continue
  
if __name__ == '__main__':
    newCrawler = threadedCrawler("https://rescale.com/", 3)
    newCrawler.crawl()




