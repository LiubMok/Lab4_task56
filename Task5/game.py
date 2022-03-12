"""
The python module that has all code that is needed for playing the game.
"""


class Room:
    """
    Class for creating a object - room, where all actions will be played.
    """

    def __init__(self, name) -> None:
        """
        Get the next parameters for an object of the class.
        :param name: name of the room.
        """
        self.name = name
        self.description = None
        self.item = None
        self.enemies = None
        self.linked_rooms = []
        self.character = None

    def set_description(self, description):
        """
        A setter that get the description of the room.
        :param description: description of the room
        """
        self.description = description

    def get_description(self):
        """
        A typical getter for the description of the room.
        """
        return self.description

    def link_room(self, neighbour_room, direction):
        """
        A method that creates links between objects in the Room class.
        :param neighbour_room: an object of the class Room.
        :param direction: direction in which the link will be.
        """
        self.linked_rooms.append((neighbour_room, direction))
        self.description += f"\nThe {neighbour_room.name} is {direction}"

    def set_character(self, character):
        """
        A setter that get the character in the room.
        :param character: an object of class Enemy.
        """
        self.character = character

    def get_character(self):
        """
        A typical getter that return a character -
        object of the class Enemy
        """
        return self.character

    def set_item(self, item):
        """
        A setter that receives item
        :param item: an object of the class Item
        """
        self.item = item

    def get_item(self):
        """
        A getter for returning an Item class object
        """
        return self.item

    def get_details(self):
        """
        A getter for printing details about the room.
        """
        details = f'{self.name}\n' \
                  f'------------------------------\n' \
                  f'{self.description}'
        print(details)

    def move(self, direction):
        """
        A method for moving from one room to another one.
        :param direction: where to go
        """
        for direct in self.linked_rooms:
            if direct[1] == direction:
                return direct[0]


class Character:
    """
    A special class that will count haw many wins has our character.
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Character, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        """
        A constructor.
        """
        self.wins = 0

    def register_new_win(self):
        """
        A method that plus 1 if the character win the fight.
        """
        self.wins += 1
        return self.wins


class Enemy:
    """
    A class for creating an object that is an enemy for the character.
    """

    def __init__(self, name, description) -> None:
        """
        A constructor of enemy object with next parameters:
        :param name: name of the object
        :param description: of the object
        """
        self.name = name
        self.description = description
        self.replica = None
        self.weakness = None
        self.counter_of_wins = Character()

    def set_conversation(self, replica):
        """
        A typical setter that receive replica of the object.
        :param replica: what the object will say if player writes "talk"
        """
        self.replica = replica

    def set_weakness(self, weakness):
        """
        A typical setter that receive weakness of the object.
        :param weakness: stm that can kill an enemy.
        """
        self.weakness = weakness

    def describe(self):
        """
        A getter that gives a description of the enemy object.
        """
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """
        A  getter to return the replica of the enemy object.
        """
        return self.replica

    def fight(self, weapon) -> bool:
        """
        A method that checks whether the weapon which the character wants to fight
        is a weakness of the enemy object.
        :param weapon: thing the character wants to fight the enemy.
        :return: bool
        """
        return weapon == self.weakness

    def get_defeated(self):
        """
        A getter that gives the counter of wins that our character done
        and add new one.
        """
        return self.counter_of_wins.register_new_win()


class Item:
    """
    A class for creating object item that is used like a weapon by the character.
    """

    def __init__(self, name) -> None:
        """
        A constructor of the Item class that has the next parameters:
        :param name: of the item
        """
        self.name = name
        self.description = None

    def set_description(self, description):
        """
        A setter that receives the description of the item.
        :param description: of the item
        """
        self.description = description

    def describe(self):
        """
        A getter to give a description of the item
        """
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        """
        A getter to give a name of the item
        """
        return self.name

    class Friend:
        """
        A class to create a friend object.
        """
        def __init__(self, name, replica) -> None:
            """
            A constructor to create an object.
            :param name: of the friend
            :param replica: of the friend
            """
            self.name = name
            self.replica = replica

        def __str__(self) -> str:
            """
            A method that return string about the friend.
            """
            return f'My name is {self.name}.{self.replica}'
