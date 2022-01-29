from multiprocessing import connection
from bs4 import BeautifulSoup
from selenium import webdriver
import sqlite3
import time

dataURL = input('\nENTER URL: ')
print('\nRETRIEVING HTML...')

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

driver = webdriver.Chrome()
driver.get(dataURL)
page = driver.page_source

data = BeautifulSoup(page, 'html.parser')
print('\nRETRIEVAL SUCCESSFUL\n\nRETRIEVING PRODUCTS...')

driver.quit()

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

    obj.availability = product.retrieveAttribute(
        tag, 
        'span', 
        'container_1DAvI'
    )

    obj.price = product.retrieveAttribute(
        tag, 
        'span', 
        'screenReaderOnly_3anTj'
    )

    print(obj.name, ' - ', obj.availability, ' - ', obj.price,)

    cursor.execute('INSERT INTO Status (availability) VALUES (?)', (obj.availability, ))
    cursor.execute('SELECT id FROM Status WHERE availability = ?', (obj.availability, ))
    status_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO Product (name, price, status_id) VALUES (?, ?, ?)', (obj.name, obj.price, status_id))

cursor.close()
conn.commit()

print('\nRETRIEVAL SUCCESSFUL')
