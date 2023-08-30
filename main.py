#! /usr/bin/env python3

# using the lxml parser 

# test to check permissions granted to the file
# print('hello world')

from bs4 import BeautifulSoup
import requests
url = 'https://www.tutorialspoint.com/index.htm'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
print(soup.title)