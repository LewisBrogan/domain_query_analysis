import logging

from utils.write_to_csv__utils import write_to_csv
from utils.fetch_trends__utils import fetch_trends

from datetime import date

def main():
    """Main function."""
    try:
        current_date = date.today()
        csv_name = f'{current_date}_daily_trends_usa.csv'
        trends_data = fetch_trends()

        if trends_data:
            write_to_csv(csv_name, trends_data)
        logging.info('File saved as: %s', csv_name)
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {str(e)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
