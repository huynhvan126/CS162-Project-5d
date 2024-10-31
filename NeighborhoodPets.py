# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/30/2024
# Description: Write a class named NeighborhoodPets that manage a collection of pet within the neighborhood. It offers to add, remove a pet, search for pet owners, and persist data to and from JSON files.
import json

class DuplicateNameError(Exception):
    """
    Exception raised when a duplicate name is encountered.
    """
    pass
class NeighborhoodPets:
    """
    A class to manage a collection of neighborhood pets, allowing users to add, delete, and retrieve pet information.
    """
    def __init__(self):
        """
        Initialize the NeighborhoodPets class with an empty collection of pets.
        """
        self._pets = {}

    def add_pet(self, pet_name: str, species: str, owner_name: str):
        """
        Add a pet to the collection.
        """
        if pet_name in self._pets:
            raise DuplicateNameError(f"A pet with name '{pet_name}' already exists.")

        self._pets[pet_name] = {"species": species, "owner": owner_name}

    def delete_pet(self, pet_name: str):
        """
        Delete a pet from the collection.
        """
        if pet_name in self._pets:
            del self._pets[pet_name]

    def get_owner(self, pet_name: str) ->str:
        """
        Get the owner of a pet.
        """
        return self._pets[pet_name]["owner"] if pet_name in self._pets else None

    def save_as_json(self, filename: str):
        """
        Save the collection to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self._pets, file, indent=4)

    def read_json(self, filename: str):
        """
        Load the collection from a JSON file.
        """
        with open(filename, 'r') as file:
            self._pets = json.load(file)

    def get_all_species(self) ->set:
        """
        Return a set of all species.
        """
        return {pet_info["species"] for pet_info in self._pets.values()}