# rescaleCrawler

This is a web crawler built as a project for rescale!

It is written in python3 mainly using BeautifulSoup, Requests, and concurrent.futures libaries!

I developed this in a Windows environment so without a MacOS or Linux enviornment to test in, I thought the safest way to share it with you guys would just be with a virtual environment, the python script and a requirements file!

If you are now safely in a virtual enviroment, the following two commands will let you see the crawler in action! 

`pip install -r requirements.txt`
`python3 rescaleCrawler.py`

The current starting point is the rescale homepage, and it crawls to a depth of 3. Both of those variables can be changed in the code!

The following command will run the tests:

`python3 tests.py`

Hope you enjoy!
