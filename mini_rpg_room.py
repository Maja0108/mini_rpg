class Room:
    """Room class of mini RPG game

    Attr:
        name (str) -- name of the room
        description (str) -- description of the room
        linked_room (str) --shows which rooms are connected
        character (str) -- shows which character is in the room
        item (str) -- shows which item is in the room

    Methods:
        set_description(description) : set the description of the room
        get_description : return the description of the room
        set_name(name) : set the name of the room 
        get_name : return the name of the room
        describe : print description
        link_room(room_to_link, direction) : connect rooms together
        get_details : print name of room, description and linked rooms
        move(direction) : move player from one room to another
        set_character(character) : set character to a room
        get_character : return the character connected to a room
        set_item(item) : set item to a room
        get_item : return the item connected to the room  
    """

    def __init__(self, room_name):
        """Initialize Room class

        Arguments:
            room_name (str) : name of the room
        """
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, room_description):
        """set the description of the room

        Args:
            room_description (str): description of the room
        """
        self.description = room_description

    def get_description(self):
        """return the description of the room

        Returns:
            str: description
        """
        return self.description

    def set_name(self, room_name):
        """Set the name of the room

        Args:
            room_name (str): name  of the room
        """
        self.name = room_name

    def get_name(self):
        """Return the name of the room

        Returns:
            str: description
        """
        return self.name

    def describe(self):
        """Print out the description of the room
        """
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Connect rooms together, to create the map of rooms

        Args:
            room_to_link (object): instance of the Room class
            direction (str): direction e.g. south
        """
        self.linked_rooms[direction] = room_to_link
        # print(self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        """Print out the name, the description of the room, and the connected rooms.
        """
        print(self.name)
        print(10 * "-" + "\n")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        print("\n")

    def move(self, direction):
        """Move Player from one room to another or warn of this movement is not available.

        Args:
            direction (str): direction e.g. south            

        Returns:
            object: instance of the next room
            str : if Player can not move, it prints out a warning
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, character):
        """Connect the character to the room.

        Args:
            character (object): instance of the Character class
        """
        self.character = character

    def get_character(self):
        """Return the character connected to the room.

        Returns:
            object: instance of the Character class connected to a room
        """
        return self.character

    def set_item(self, item):
        """
        Connect item to a room

        Args:
            item (object): instance of the Items class
        """
        self.item = item

    def get_item(self):
        """Return the item connected to the room.

        Returns:
            object: instance of the Items class connected to a room
        """
        return self.item
