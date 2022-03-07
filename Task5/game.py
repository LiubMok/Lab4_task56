class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.item = None
        self.enemies = None
        self.linked_rooms = []
        self.character = None

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def link_room(self, neighbour_room, direction):
        self.linked_rooms.append((neighbour_room, direction))
        self.description += f"\nThe {neighbour_room.name} is {direction}"

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def get_details(self):
        details = f'{self.name}\n' \
                  f'------------------------------\n' \
                  f'{self.description}'
        print(details)

    def move(self, direction):
        for direct in self.linked_rooms:
            if direct[1] == direction:
                return direct[0]


class Wins:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Wins, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.wins = 0

    def register_new_win(self):
        self.wins += 1
        return self.wins


class Enemy:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.replica = None
        self.weakness = None
        self.counter_of_wins = Wins()

    def set_conversation(self, replica):
        self.replica = replica

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        return self.replica

    def fight(self, weapon):
        return weapon == self.weakness

    def get_defeated(self):
        return self.counter_of_wins.register_new_win()


class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name
