from bs4 import BeautifulSoup

with open('.\\test_images\\Datasheets_all.html', 'r', encoding='utf-8') as datasheets:
    soup = BeautifulSoup(datasheets, 'html.parser');

datasheetsArr = [];

# for anchor in 

