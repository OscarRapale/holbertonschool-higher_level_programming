import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.

    Parameters:
    - dictionary (dict): The dictionary to serialize.
    - filename (str): The name of the file to save the serialized XML data.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)

        return True

    except Exception as e:
        print(f"An error occurred during serialization: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Read XML data from a file and return a deserialized Python dictionary.

    Parameters:
    - filename (str): The name of the file to read the XML data from.

    Returns:
    - dict: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {child.tag: child.text for child in root}

        return dictionary

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None
