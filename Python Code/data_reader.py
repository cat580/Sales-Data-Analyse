import csv

def read_data(input_file):
    """Read data from CSV file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Print column names for debugging
            print("Available columns:", reader.fieldnames)
            data = list(reader)
            if not data:
                return None
            return data
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")