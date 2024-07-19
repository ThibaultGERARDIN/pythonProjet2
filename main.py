from extract_books_urls import extract_books_urls
from extract_book_infos import extract_book_infos
from extract_categories import extract_categories
from save_csv import save_csv
from save_img import save_img

# Gets the list of categories (name and url)
categories_list = extract_categories()

# loops for each category in the list
for category in categories_list:
    
    # Gets the url of the category page
    category_url = category['category_url']
    # gets the name of the category to construct the name of the csv file to save in csv_files folder
    category_name = category['category_name']
    file_name = './csv_files/' + category_name.lower().replace(' ','_') + '.csv'
    # extracts the urls of all the books in the category
    books_urls = extract_books_urls(category_url)
    # loops on the list of urls to extract the informations and store them in the current category info list
    current_category_infos = []
    for book_url in books_urls:
        book_info = extract_book_infos(book_url)
        current_category_infos.append(book_info)
        book_title = book_info['title']
        image_url = book_info['image_url']
        save_img(book_title, image_url, category_name)
    # saves all of the gathered information in a csv file
    save_csv(file_name, current_category_infos)

    





