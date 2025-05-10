"""
Module for reading sales data from CSV files.
No external dependencies required.
"""
import csv

def read_data(input_file):
    """
    Read data from CSV file and return as a list of dictionaries.
    
    Args:
        input_file (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries containing the sales data, or None if error
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("Available columns:", reader.fieldnames)
            data = list(reader)
            if not data:
                return None
            return data
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None