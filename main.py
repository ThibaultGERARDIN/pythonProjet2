from bs4 import BeautifulSoup
import requests
import csv

from extract_books_urls import extract_books_urls
from extract_book_infos import extract_book_infos

category_url ='http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'

books_urls = extract_books_urls(category_url)

current_category_infos = []

for book_url in books_urls:
    book_info = extract_book_infos(book_url)
    current_category_infos.append(book_info)






with open('test.csv', 'w', newline='') as fichier_csv:
    headers = [
        'product_page_url', 
        'universal_ product_code', 
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
    writer.writerows(current_category_infos)





