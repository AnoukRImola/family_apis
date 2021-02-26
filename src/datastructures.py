
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky Numbers": [7, 13, 22], #un key no puede tener varios valores
                "keyid": self._generateId()
            },

            {
                "name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky Numbers": [10, 14, 3], #un key no puede tener varios valores
                "keyid": self._generateId()
            },

            {
                "name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky Numbers": [1], #un key no puede tener varios valores
                "keyid": self._generateId()
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, name, age, lucky_numbers): #agrega un miembro nuevo
        # fill this method and update the return
        member = {
                "name": name,
                "last_name": self.last_name,
                "age": age,
                "lucky Numbers": lucky_numbers
        }
        self._members.append(member)
        return "Se agrego correctamente un miembro"


    def delete_member(self, id):
        # fill this method and update the return
        for item in self._members:
            if id == item["keyid"]:
                return item
        self._members.remove(item)
        return "Se elimino un miembro corectamente"        

    def get_member(self, id): #funcion que me otorga la informacion de una perosna ya agregada(tota la info)
        # fill this method and update the return
        for item in self._members:
            if id == item["keyid"]:
                return item
        
        return item     

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
