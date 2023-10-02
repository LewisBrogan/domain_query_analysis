"""
This module provides the `write_to_csv_region_name` function, 
which writes the region names data to a CSV file.

Functions:
    - write_to_csv_region_name(file_name: str, data: List[str]) -> None: 
        Writes region name to a CSV file.
"""

import logging
import csv

from typing import List

def write_to_csv_region_name(file_name: str, data: List[str]) -> None:
    """Write Region name to a CSV file."""
    logging.info('Writing region names data to CSV file...')
    with open(file_name, encoding='utf-8', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Region Name'])
        for region_names in data:
            writer.writerow([region_names])
    logging.info('Region names data written to CSV file...')
