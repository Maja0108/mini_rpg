class Characters:
    """
    Set parameter of Characters class. It has child classes as Enemy and Friend.
    
    Attr:
    name (str) -- name of the item
    char-description (str) -- description of the item
    conversation (str) -- what the character talks about
    weakness (str) -- what weapon is useful against it
    """

    def __init__(self, char_name, char_description):
        """Initialize Character class

        Args:
            char_name (str) : name of the character
            char_description ([type]): [description]
        """
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.weakness = None

    def describe(self):
        """print the name and the description of the character 
        """
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Set what this character will say when talked to

        Args:
            conversation (str):  what this character will say when talked to
        """
        self.conversation = conversation

    def talk(self):
        """Talk to this character
        """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Fight with this character

        Args:
            combat_item (str): accesible weapons are in the backpack

        Returns:
            boolean: tells the end of the fight
        """
        if combat_item == self.weakness:
            print(
                "You make a new friend, "
                + self.name
                + ". A(n) "
                + combat_item
                + " was used."
            )
            return True
        elif combat_item in [" "]:
            print(self.name + " is not happy. Try again.")
            return False

        else:
            print(self.name + " doesn't want to fight with you")
            return True


class Enemy(Characters):
    """
    Childclass of Characters, they are the ones the Player has to fight with.
    """

    def __init__(self, char_name, char_description):
        """Initialize Enemy class

        Args:
            char_name (str): name of the enemy
            char_description (str): description of the enemy
        """
        super().__init__(char_name, char_description)

    def set_weakness(self, weakness):
        """Set the weakness of the enemy. This helps to defeat the enemy.

        Args:
            weakness (str): weakness of the enemy
        """
        self.weakness = weakness

    def get_weakness(self):
        """Return weakness of the enemy

        Returns:
            str: weakness
        """
        return self.weakness


class Friend(Characters):
    "Childclass of Characters class"

    def __init__(self, char_name, char_description):
        """Initialize Friend class

        Args:
            char_name (str): name of the enemy
            char_description (str): description of the enemy
        """
        super().__init__(char_name, char_description)

    def set_interest(self, interest):
        """Interests of the friends

        Args:
            interest (str): interest of the friend
        """
        self.interest = interest

    def get_interest(self):
        """Return interests of the friends

        Returns:
            str: interest of the friend
        """
        return self.interest
