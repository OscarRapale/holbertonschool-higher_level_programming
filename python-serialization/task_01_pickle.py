import pickle

class CustomObject:
    """
    A custom Python class that represents an object with a name, age, and student status.

    Attributes:
    name (str): The name of the object.
    age (int): The age of the object.
    is_student (bool): The student status of the object.
    """

    def __init__(self, name, age, is_student):
        """
        The constructor for CustomObject class.

        Parameters:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): The student status of the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the object in a formatted manner.

        Returns:
        None
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object and saves it to a file.

        Parameters:
        filename (str): The name of the file to save the serialized object to.

        Returns:
        None
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of the CustomObject from a file.

        Parameters:
        filename (str): The name of the file to load the object from.

        Returns:
        CustomObject: The deserialized object.
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
