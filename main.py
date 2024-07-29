import tqdm
from extract_books_urls import extract_books_urls
from extract_book_infos import extract_book_infos
from extract_categories import extract_categories
from save_csv import save_csv
from save_img import save_img

# Gets the list of categories (name and url)
categories_list = extract_categories()

# Sets up main counter for the progress bar + current category display
outer = tqdm.tqdm(total=len(categories_list), desc='Scraping categories', position=0)
category_log = tqdm.tqdm(total=0, position=1, bar_format='{desc}')

# loops for each category in the list
for category in categories_list:

    # Gets the url of the category page
    category_url = category['category_url']
    # gets the name of the category (used for the csv file and image folder)
    category_name = category['category_name']
    # Sets the name of the current category to the progress display
    category_log.set_description_str(f'Current category: {category_name}')
    # extracts the urls of all the books in the category
    books_urls = extract_books_urls(category_url)
    # Sets progress bar for books in category
    inner = tqdm.tqdm(total=len(books_urls), desc = f'Books in {category_name}', leave= None, position = 2)
    # loops on the list of urls to extract the informations and store them in the current category info list
    current_category_infos = []
    for book_url in books_urls:
        book_info = extract_book_infos(book_url)
        current_category_infos.append(book_info)
        book_title = book_info['title']
        image_url = book_info['image_url']
        save_img(book_title, image_url, category_name)
        inner.update(1)
    # saves all of the gathered information in a csv file
    save_csv(category_name, current_category_infos)
    outer.update(1)

    





