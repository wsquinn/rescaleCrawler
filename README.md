# rescaleCrawler

This is a web crawler built as a project for rescale!

It is written in python3 mainly using BeautifulSoup, Requests, and concurrent.futures libaries!

I developed this in a Windows environment so without a MacOS or Linux enviornment to test in, I thought the safest way to share it with you guys would just be with a virtual environment, the python script and a requirements file!

If you are now safely in a virtual enviroment, the following two commands will let you see the crawler in action! 

`pip install -r requirements.txt`
and then
`python3 rescaleCrawler.py https://rescale.com/` or `python rescaleCrawler.py https://rescale.com/`

The current example is the rescale homepage, and it will crawl indefinitely (or until it reaches dead ends).

There is an optional second argument to limit the maximum depth of the crawl (how many layers down) that can be specified such as:

`python3 rescaleCrawler.py https://rescale.com/ 3`

which would limit the crawl to a depth of 3. If not specified, the crawler wil run indefinitely. 

The following command will run the tests:

`python3 test.py` or `python test.py`

The results of this test will write out to log_file.txt

Hope you enjoy!
