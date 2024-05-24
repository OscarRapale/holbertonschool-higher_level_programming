#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    An abstract base class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses to return the sound that the animal makes.
        """
        pass

class Dog(Animal):
    """
    A class representing a dog, inheriting from the Animal abstract base class.
    """
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """
    A class representing a cat, inheriting from the Animal abstract base class.
    """
    def sound(self):
        return "Meow"
