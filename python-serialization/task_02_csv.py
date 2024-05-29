import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to JSON format.

    Parameters:
    filename (str): The name of the CSV file to convert.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(filename, 'r') as csv_file:
            # Convert each row into a dictionary
            data = list(csv.DictReader(csv_file))

        with open('data.json', 'w') as json_file:
            # Serialize the list of dictionaries
            json.dump(data, json_file)

        # Conversion was successful
        return True

    except Exception:
        # An error occurred
        return False
