from bs4 import BeautifulSoup
import requests


def extract_books_urls(category_url):
    
    """
    Function used to extract the urls of all the books in the given category (category_url)
    Returns a list of all urls
    """

    # Initialize the parameters :
    # Gets the url of the category we're scraping
    current_category_url = category_url
    # Requests the page from the url above
    category_page = requests.get(current_category_url)
    # Parses the html content
    soup = BeautifulSoup(category_page.content, 'html.parser')
    # Gets every book in the page (from the miniatures)
    books_list = soup.find_all('div', class_='image_container')
    # Gets the "next" button if it exists
    next = soup.find('li', class_='next')
    # Initialize the list of all the book urls in the page
    books_urls = []

    # If next exists then starts the loop to get every page
    if next:
        # Loops while the "next" button exists on the page
        while next:
            # Gets each book's url and adds it to the list
            for book in books_list:
                # gets the relative url from the link
                book_relative_url = book.a['href']
                # replace relative path with absolute path
                book_url = book_relative_url.replace('../../../', 'http://books.toscrape.com/catalogue/')
                # adds the url to the list
                books_urls.append(book_url)
          
            # next page gets the last bit of the href link (page_2 / page_3 / etc)
            next_page = next.a['href'].rsplit('/', 1)[-1]
            # gets the last bit of the current url (index.html / page_2 / etc)
            current_page = current_category_url.rsplit('/', 1)[-1]
            # replaces the current url with the next page (by replacing only the end)
            current_category_url = current_category_url.replace(current_page, next_page)
            # updates all the initial parameters with the next page's url:
            category_page = requests.get(current_category_url)
            soup = BeautifulSoup(category_page.content, 'html.parser')
            books_list = soup.find_all('div', class_='image_container')
            next = soup.find('li', class_='next')
        # makes the script loop the last page (the while loop breaks on last page, because "next" doesn't exist anymore)
       
        for book in books_list:
            book_relative_url = book.a['href']
            book_url = book_relative_url.replace('../../..', 'http://books.toscrape.com/catalogue')
            books_urls.append(book_url)

    # If next doesn't exist then loops the current page
    else:
        for book in books_list:
            book_relative_url = book.a['href']
            book_url = book_relative_url.replace('../../..', 'http://books.toscrape.com/catalogue')
            books_urls.append(book_url)

    return books_urls


