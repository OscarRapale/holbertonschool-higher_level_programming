import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the input data into JSON format and save it to a file.

    Parameters:
    data (dict): The data to be serialized.
    filename (str): The name of the file to save the serialized data to.

    Returns:
    None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load data from a file and deserialize it from JSON format.

    Parameters:
    filename (str): The name of the file to load the data from.

    Returns:
    dict: The deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
