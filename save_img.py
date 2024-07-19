import urllib.request
import os

def save_img(book_title, image_url, category_name):

    """ 
    Function used to save the image of a book in the images folder with the title of the book as name 
    """
    
    # Creates the name of the image file out of title of book (replacing all "problematic" characters)
    img_name = book_title.lower().replace(' ','_').replace(':','_').replace('/','_').replace('\\','_').replace('"','').replace('<','_').replace('>','_').replace('?','').replace('*','').replace('|','_')
    # Creates subfolder name out of category name
    sub_folder = category_name.lower().replace(' ','_') + '/'
    # Creates the path of the image file to save
    img_path = './images/' + sub_folder
    # Creates a sub folder for the category (if it doesn't exist yet)
    if not os.path.isdir(img_path):
        os.makedirs(img_path)
    # Creates the full path
    file_path = img_path + img_name + '.jpg'

    urllib.request.urlretrieve(image_url, file_path)