import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML and saves it to a file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML data to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and deserializes it into a dictionary.

    Parameters:
    filename (str): The name of the file to read the XML data from.

    Returns:
    dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = convert_str(child.text)
    return dictionary


def convert_str(s):
    """
    Tries to convert a string to an integer, a float, or a boolean.
    If all conversions fail, returns the original string.

    Parameters:
    s (str): The string to convert.

    Returns:
    int/float/bool/str: The converted value.
    """
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if s.lower() == 'true':
                return True
            elif s.lower() == 'false':
                return False
            else:
                return s
