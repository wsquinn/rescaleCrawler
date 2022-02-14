import unittest

from rescaleCrawler import threadedCrawler


class rescaleCrawler(unittest.TestCase):
    def initialReturn(self):
        """
        Test that it can sum a list of integers
        """
        url = 'https://rescale.com/'
        depth = 0
        newCrawler = threadedCrawler(url, depth)
        
        self.assertEqual(newCrawler.linksSeens, 1)

    # def test_list_fraction(self):
    #     """
    #     Test that it can sum a list of fractions
    #     """
    #     data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
    #     result = sum(data)
    #     self.assertEqual(result, 1)

if __name__ == '__main__':
    url = 'https://rescale.com/'
    depth = 2
    newCrawler = threadedCrawler(url, depth)
    #print(newCrawler.linksSeen)
    assert newCrawler.linksSeen == 1