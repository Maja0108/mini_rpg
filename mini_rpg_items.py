class Items:
    """
    Class of RPG items
    
    Attr:
        name (str) -- name of the item
        description (str) -- description of the item
        location (str) -- location of the item

    Methods:
        set_description(description) : set the description of the item
        get_description : return the description of the item
        describe : print description
        get_details : print name of item, description and linked rooms
    """

    def __init__(self, item_name):
        """initialize Items class

        Args:
            item_name (str): name of the item
        """
        self.name = item_name
        self.description = None
        self.location = None

    def set_description(self, description):
        """set the description of the item

        Args:
            description (str): description of the item
        """
        self.description = description

    def get_description(self):
        """return the description of the item

        Returns:
            str: description
        """
        return self.description

    def describe(self):
        """Print out the description of the item
        """
        print(self.description)

    def get_details(self):
        """Print out the description of the item, and the location of the item.
        """
        print(self.description)
        print(self.location)
