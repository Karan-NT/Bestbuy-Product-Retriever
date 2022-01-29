from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium import webdriver
import sqlite3
import smtplib
import time

username = input('ENTER USERNAME: ')
password = input('ENTER PASSWORD: ')

recipient = input('\nENTER RECIPIENT: ')

dataURL = input('\nENTER URL: ')

def getPage():
    print('\nRETRIEVING HTML...')

    driver = webdriver.Chrome()
    driver.get(dataURL)
    page = driver.page_source
    data = BeautifulSoup(page, 'html.parser')

    driver.quit()
    print('\nRETRIEVAL SUCCESSFUL')

    return data

newData = getPage()
oldData = newData

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

def updateDatabase():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    print('\nRETRIEVING PRODUCTS...')

    for tag in newData.find_all('div'):
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

        cursor.execute('''INSERT OR IGNORE INTO 
            Status (availability) VALUES (?)''', 
            (obj.availability, )
        )
        cursor.execute('''SELECT id FROM Status 
            WHERE availability = ?''', 
            (obj.availability, )
        )
        status_id = cursor.fetchone()[0]

        cursor.execute('''INSERT OR REPLACE INTO Product 
            (name, price, status_id) VALUES (?, ?, ?)''', 
            (obj.name, obj.price, status_id)
        )

    print('\nRETRIEVAL SUCCESSFUL')

    cursor.close()
    conn.commit()

def send():
    conn = sqlite3.connect('Database.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Product JOIN Status 
        ON Product.status_id = Status.id''')

    content = str(dataURL)
    for row in cursor.fetchall():
        content = content + '\n' + str(row)

    msg = MIMEText(content)
    msg['Subject'] = 'Update on tracked products'
    msg['From'] = username
    msg['To'] = recipient

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(
            username, 
            [recipient], 
            msg.as_string()
        )
        print('\nMAIL SENT SUCCESSFULLY')
        server.quit()
    except:
        print('\nFAILED TO SEND MAIL')
        server.quit()

while True:
    updateDatabase()
    send()
    while oldData == newData:
        time.sleep(600)
        newData = getPage()
    oldData = newData
