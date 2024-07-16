from bs4 import BeautifulSoup
import requests
import csv

product_page_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
page = requests.get(product_page_url)
soup = BeautifulSoup(page.content, 'html.parser')


# for the infos in the table
td_list = []

for tr in soup.find_all('tr'):
    td = tr.find('td')
    td_list.append(td.string)

upc = td_list[0]
price_including_tax = td_list[2]
price_excluding_tax = td_list[3]

# get the number available from the availability string
availability = td_list[5]
number_available = int(''.join(filter(str.isdigit, availability)))

# gets the title from h1 tag
title = soup.h1.string
# gets the description from the only p tag without a class (using index 0 to extract the text)
product_description = soup.find_all('p', class_='')[0].get_text()
# gets the category from the links at the top
category = soup.find_all('li')[2].get_text()
# gets the image url from its src attribute
image_url = soup.find('img')['src']


# for the rating, extract the information out of the class for the stars
if soup.find_all('p', class_='One'):
    review_rating = '1/5'
elif soup.find_all('p', class_='Two'):
    review_rating = '2/5'
elif soup.find_all('p', class_='Three'):
    review_rating = '3/5'
elif soup.find_all('p', class_='Four'):
    review_rating = '4/5'
elif soup.find_all('p', class_='Two'):
    review_rating = '5/5'

# construc a dictionnary from all the different informations gathered
infos = {
    'product_page_url':product_page_url,
    'upc': upc,
    'title': title,
    'price_including_tax': price_including_tax,
    'price_excluding_tax': price_excluding_tax,
    'number_available': number_available,
    'product_description': product_description,
    'category': category,
    'review_rating': review_rating,
    'image_url': image_url
}

with open('test.csv', 'w', newline='') as fichier_csv:
    headers = [
        'product_page_url', 
        'upc', 
        'title', 
        'price_including_tax', 
        'price_excluding_tax', 
        'number_available',
        'product_description',
        'category',
        'review_rating',
        'image_url'
        ]
    writer = csv.DictWriter(fichier_csv, fieldnames=headers)
    writer.writeheader()
    writer.writerow(infos)

with open('test.csv', 'r') as test_csv:
    reader = csv.DictReader(test_csv, delimiter=',')
    for ligne in reader:
        print(ligne)




