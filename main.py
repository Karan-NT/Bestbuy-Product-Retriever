import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import time

dataURL = input('ENTER URL: ')
print('\nRETRIEVING HTML...')

dataRequest = urllib.request.Request(
    dataURL, 
    headers = {'User-Agent': 'Mozilla/5.0'}
)
dataOpen = urllib.request.urlopen(dataRequest).read()
data = BeautifulSoup(dataOpen, 'html.parser')
print('\nRETRIEVAL SUCCESSFUL')

products = dict()

for tag in data.find_all('div'):
    if tag.get('class') == 'productItemName_3IZ3c':
        avai = ''
        for child in tag.parent.descendants:
            if child.get('class') == 'container_1DAvI':
                avai = child.text
        products[tag] = avai