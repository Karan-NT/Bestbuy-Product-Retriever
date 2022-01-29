from bs4 import BeautifulSoup
from selenium import webdriver
import time

dataURL = input('\nENTER URL: ')
print('\nRETRIEVING HTML...')

driver = webdriver.Chrome()
driver.get(dataURL)
page = driver.page_source
data = BeautifulSoup(page, 'html.parser')
print('\nRETRIEVAL SUCCESSFUL\n\nRETRIEVING PRODUCTS...')

li = list()
class product:
    name = ''
    availability = ''
    price = ''

    def retrieveAttribute(startingTag, targetTag, targetClass):
        for child in startingTag.parent.parent.find_all(targetTag):
            try: child.get('class')
            except: continue

            if ( (type(child.get('class'))) == type(li) and 
                targetClass in child.get('class')
            ): return child.text

for tag in data.find_all('div'):
    try: tag.get('class')
    except: continue

    if ( (type(tag.get('class'))) == type(li) and 
        'productItemName_3IZ3c' in tag.get('class')
    ): pass
    else: continue

    obj = product()
    obj.name = tag.text
    obj.availability = product.retrieveAttribute(tag, 'span', 'container_1DAvI')
    obj.price = product.retrieveAttribute(tag, 'span', 'screenReaderOnly_3anTj large_3aP7Z')
    print(obj.name, obj.availability, obj.price)

driver.quit()
#print('\nRETRIEVAL SUCCESSFUL\n\n', li)