import logging

from utils.write_to_csv__utils import write_to_csv
from utils.fetch_trends__utils import fetch_trends
# from utils.move_data_to_region_folder__utils import move_file_to_region_folder

from datetime import date

def main():
    """Main function."""
    try:
        regions = ['uk', 'us']
        current_date = date.today()

        for region_code in regions:
            trends_data = fetch_trends(region_code)
            csv_name = f'{current_date}_daily_trends_{region_code}.csv'

            if trends_data:
                write_to_csv(csv_name, trends_data)
                logging.info('File saved as: %s', csv_name)

               # move_file_to_region_folder(csv_name, region_code)


    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {str(e)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
