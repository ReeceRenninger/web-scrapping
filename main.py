#! /usr/bin/env python3

# using the lxml parser 

# test to check permissions granted to the file
# print('hello world')

#! test example 
from bs4 import BeautifulSoup
import requests
url = 'https://github.com/ReeceRenninger'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
print(soup.title) #should return <title>ReeceRenninger (Reece Renninger) · GitHub</title>

