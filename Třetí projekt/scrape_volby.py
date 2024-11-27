"""
projekt_3.py: Třetí projekt do Engeto Online Python Akademie
author: Mykola Tichonov
email: mykola.tikhonov@seznam.cz
discord: phranschyze
"""

import argparse
from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.parse import urljoin

def scrape_data(url, output_file):
    try:
        # Fetch the main page content
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all tables with the class 'table'
    tables = soup.find_all('table', class_='table')

    all_data = []
    headers = ['code', 'location', 'registered', 'envelopes', 'valid']

    # Dynamically fetch additional column names
    dynamic_columns_t1 = []
    dynamic_columns_t2 = []
    for table in tables:
        rows = table.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 1:
                # Fetch dynamic columns from the linked page for both header types
                additional_columns_t1 = fetch_dynamic_columns(cells[0], url, 't1sa1 t1sb2', 't1sa2 t1sb3')
                additional_columns_t2 = fetch_dynamic_columns(cells[0], url, 't2sa1 t2sb2', 't2sa2 t2sb3')
                dynamic_columns_t1.extend(additional_columns_t1)
                dynamic_columns_t2.extend(additional_columns_t2)

    # Remove duplicates and sort the dynamic columns
    dynamic_columns_t1 = sorted(set(dynamic_columns_t1), key=dynamic_columns_t1.index)
    dynamic_columns_t2 = sorted(set(dynamic_columns_t2), key=dynamic_columns_t2.index)
    headers.extend(dynamic_columns_t1)
    headers.extend(dynamic_columns_t2)

    # Extract data from each table
    for table in tables:
        rows = table.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 1:
                code = cells[0].text.strip()
                location = cells[1].text.strip()
                registered = get_registered_value(cells[0], url)
                envelopes = get_envelopes_value(cells[0], url)
                valid = get_valid_value(cells[0], url)

                # Initialize dynamic columns with empty values
                dynamic_data_t1 = {col: "" for col in dynamic_columns_t1}
                dynamic_data_t2 = {col: "" for col in dynamic_columns_t2}

                # Fetch values for dynamic columns from the linked page
                for i, col in enumerate(dynamic_columns_t1):
                    dynamic_data_t1[col] = get_dynamic_value(cells[0], url, i, 't1sa2 t1sb3')
                for i, col in enumerate(dynamic_columns_t2):
                    dynamic_data_t2[col] = get_dynamic_value(cells[0], url, i, 't2sa2 t2sb3')

                # Combine static and dynamic data
                data_row = [code, location, registered, envelopes, valid]
                data_row.extend(dynamic_data_t1.values())
                data_row.extend(dynamic_data_t2.values())

                all_data.append(data_row)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(all_data, columns=headers)
    try:
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def fetch_dynamic_columns(cell, base_url, header_type, value_header_type):
    """
    Fetch additional column names dynamically from the linked page.
    Extract names from <td class="overflow_name" headers="..."> elements.
    """
    link = cell.find('a')
    if link:
        relative_url = link['href']
        absolute_url = urljoin(base_url, relative_url)
        try:
            page = requests.get(absolute_url)
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'html.parser')

            # Find all names for the dynamic columns based on the header type
            column_cells = soup.find_all('td', class_='overflow_name', headers=header_type)
            dynamic_columns = [cell.text.strip() for cell in column_cells]
            return dynamic_columns
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL {absolute_url}: {e}")
    return []

def get_registered_value(cell, base_url):
    return get_value_from_page(cell, base_url, 'sa2')

def get_envelopes_value(cell, base_url):
    return get_value_from_page(cell, base_url, 'sa3')

def get_valid_value(cell, base_url):
    return get_value_from_page(cell, base_url, 'sa6')

def get_value_from_page(cell, base_url, header_id):
    """
    Generalized function to fetch a value from a linked page based on the header ID.
    """
    link = cell.find('a')
    if link:
        relative_url = link['href']
        absolute_url = urljoin(base_url, relative_url)
        try:
            page = requests.get(absolute_url)
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'html.parser')
            value_cell = soup.find('td', class_='cislo', headers=header_id)
            if value_cell:
                return value_cell.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL {absolute_url}: {e}")
    return ""

def get_dynamic_value(cell, base_url, index, header_id):
    """
    Fetch a value from a linked page based on the index of the dynamic column.
    """
    link = cell.find('a')
    if link:
        relative_url = link['href']
        absolute_url = urljoin(base_url, relative_url)
        try:
            page = requests.get(absolute_url)
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'html.parser')
            value_cells = soup.find_all('td', class_='cislo', headers=header_id)
            if value_cells:
                return value_cells[index].text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL {absolute_url}: {e}")
    return ""

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and save data from a URL to a CSV file.")
    parser.add_argument('url', help='URL to fetch data from')
    parser.add_argument('output_file', help='Name of the output CSV file')

    # Parse arguments
    args = parser.parse_args()

    # Run the scraping function
    scrape_data(args.url, args.output_file)
