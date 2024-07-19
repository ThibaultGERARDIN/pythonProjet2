from bs4 import BeautifulSoup
import requests

def extract_categories():
    
    """
    Function used to extract all the categories from the main page (http://books.toscrape.com/)
    Returns a list of dictionnaries containing both the name and url of each category, with the headers:
    'category_name'
    'category_url'
    """

    url = 'http://books.toscrape.com/'
    main_page = requests.get(url)
    soup = BeautifulSoup(main_page.content, 'html.parser')

    categories_list = []
    full_menu = soup.find('ul', class_='nav nav-list')
    categories_menu = full_menu.find('ul')
    categories = categories_menu.find_all('a')

    for cat in categories:
        category_name = cat.get_text().strip()
        category_url ='http://books.toscrape.com/' + cat['href']
        category ={
            'category_name': category_name,
            'category_url': category_url
        }
        categories_list.append(category)

    return categories_list