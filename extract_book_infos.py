from bs4 import BeautifulSoup
import requests

def extract_book_infos(book_url):
    
    """
    Function used to extract the information of the book from "book_url" page of Books To Scrape
    It will return a dictionnary of all the information gathered, with the headers :
    'product_page_url'
    'universal_ product_code'
    'title'
    'price_including_tax'
    'price_excluding_tax'
    'number_available'
    'product_description'
    'category'
    'review_rating'
    'image_url'
    """

    product_page_url = book_url
    page = requests.get(product_page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # gets all information contained in the table
    td_list = []

    for tr in soup.find_all('tr'):
        td = tr.find('td')
        td_list.append(td.string)

    upc = td_list[0]
    price_including_tax = td_list[2]
    price_excluding_tax = td_list[3]

    # gets the number available from the availability string
    availability = td_list[5]
    number_available = int(''.join(filter(str.isdigit, availability)))

    # gets the title from h1 tag
    if soup.h1:
        title = soup.h1.string
    else:
        title = "N/A"
    # gets the description from the only p tag without a class (using index 0 to extract the text)
    if soup.find_all('p', class_=''):
        product_description = soup.find_all('p', class_='')[0].get_text()
    else:
        product_description = "N/A"
    # gets the category from the links at the top
    if soup.find_all('li'):
        category = soup.find_all('li')[2].a.get_text().strip()
    else:
        category = "N/A"
    # gets the image url from its src attribute
    if soup.find('img'):
        image_relative_url = soup.find('img')['src']
        image_url = image_relative_url.replace('../../', 'http://books.toscrape.com/')
    else:
        image_url = "N/A"



    # for the rating, extract the information out of the class for the stars
    product_main = soup.find('div', class_='product_main')
    rating_class = product_main.find('p', class_='star-rating')['class']

    if 'One' in rating_class:
        review_rating = '1/5'
    elif 'Two' in rating_class:
        review_rating = '2/5'
    elif 'Three' in rating_class:
        review_rating = '3/5'
    elif 'Four' in rating_class:
        review_rating = '4/5'
    elif 'Five' in rating_class:
        review_rating = '5/5'

    # construct a dictionnary from all the different informations gathered
    book_infos = {
        'product_page_url':product_page_url,
        'universal_ product_code': upc,
        'title': title,
        'price_including_tax': price_including_tax,
        'price_excluding_tax': price_excluding_tax,
        'number_available': number_available,
        'product_description': product_description,
        'category': category,
        'review_rating': review_rating,
        'image_url': image_url
    }
    return book_infos






