import logging
import csv

def write_to_csv(file_name, data):
    """Write trend data to a CSV file."""
    logging.info('Writing data to CSV file...')
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Bio', 'Hits'])
        for trend in data:
            writer.writerow(trend)