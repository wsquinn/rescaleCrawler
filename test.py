import unittest
from bs4 import BeautifulSoup
import requests
import validators
from rescaleCrawler import threadedCrawler

class SimpleTest(unittest.TestCase):
  
    def test1(self):        
        url = 'https://rescale.com/'
        depth = 0
        newCrawler = threadedCrawler(url, depth)
        newCrawler.crawl()
        assert newCrawler.linksSeen == 1

    def test2(self):        
        url = 'https://books.toscrape.com/index.html'
        depth = 100
        newCrawler = threadedCrawler(url, depth)
        newCrawler.crawl()
        
  
if __name__ == '__main__':
    unittest.main()