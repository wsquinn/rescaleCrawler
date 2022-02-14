import unittest
from bs4 import BeautifulSoup
import requests
import validators
from rescaleCrawler import threadedCrawler

class SimpleTest(unittest.TestCase):
  
    #test inital crawl
    def test1(self):        
        url = 'https://rescale.com/'
        depth = 0
        newCrawler = threadedCrawler(url, depth)
        newCrawler.crawl()
        assert newCrawler.linksSeen == 1

    #check if requests working
    def test2(self):        
        url = 'https://google.com/'
        res = requests.get(url)
        assert res.status_code == 200
    
    #test deep crawl
    def test3(self):        
        url = 'https://www.brickeconomy.com/'
        depth = 3
        newCrawler2 = threadedCrawler(url, depth)
        newCrawler2.crawl()

    #check sub links are gathered correctly
    def test4(self):
        mainUrl = "https://rescale.com/"
        soup = BeautifulSoup(requests.get(mainUrl).content, "html.parser")
        subLinks = soup.find_all('a', href=True)
        validsubLinks=set()
        for link in subLinks:
            url = link['href']
            if validators.url(url):
                validsubLinks.add(url)
        newCrawler1 = threadedCrawler(mainUrl, 2)
        newCrawler1.crawl()
        print(validsubLinks)
        print(newCrawler1.cache)
        assert newCrawler1.cache == validsubLinks
    
    #test validators library
    def test5(self):
        absoluteLinks = ['https://rescale.com/', 'https://books.toscrape.com/index.html', "https://www.brickeconomy.com/sets/retiring-soon",
                        'http://rescale.com/', 'http://books.toscrape.com/index.html', "http://www.brickeconomy.com/sets/retiring-soon"]
        linksToTest = ['https://rescale.com/', 'https://books.toscrape.com/index.html', "https://www.brickeconomy.com/sets/retiring-soon",
                       'http://rescale.com/', 'http://books.toscrape.com/index.html', "http://www.brickeconomy.com/sets/retiring-soon", 
                       'http://rescalecom/', 'http:/books.toscrape.com/index.html', "htp://www.brickeconomy.com/sets/retiring-soon",
                       '/index.html', "brickeconomy.com/sets/retiring-soon"]
        validLinks = []
        for link in linksToTest:
            if validators.url(link):
                validLinks.append(link)
        assert absoluteLinks == validLinks
  
if __name__ == '__main__':
   log_file = 'log_file.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)