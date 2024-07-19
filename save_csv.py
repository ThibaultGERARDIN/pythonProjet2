import csv
import os

def save_csv(category_name, current_category_infos):

    """
    Function used to save "current_category_info" in a "file_name.csv" file located in csv_files folder 
    """
    if not os.path.isdir('./csv_files'):
        os.makedirs('./csv_files')
    file_path = './csv_files/' + category_name.lower().replace(' ','_') + '.csv'

    with open(file_path, 'w', newline='', encoding="utf-8") as fichier_csv:
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