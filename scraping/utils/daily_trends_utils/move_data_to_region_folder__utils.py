import os
import logging

def move_file_to_region_folder(csv_name, region_code):
    """Move file to region folder."""
    try:
        region_folder = f'.\scraping\data\{region_code}'
        logging.info(f'Region folder location: {region_folder}')
        os.makedirs(region_folder, exist_ok=True)
        os.rename(csv_name, os.path.join(region_folder, csv_name))
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {str(e)}")