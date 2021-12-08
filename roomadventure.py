
###################################################### 
# Name: 

# Date: 
# Description: 
###################################################### 

 
###################################################### 
# the blueprint for a room 

class Room: 

 # the constructor 
    def __init__(self, name): 
  # rooms have a name, exits (e.g., south), exit 
  #  locations (e.g., to the south is room n), items 
  #  (e.g., table), item descriptions (for each item), 
  #  and grabbables (things that can be taken into 
  #  inventory) 
        self.name = name 
        self.exits = [] 
        self.exitLocations = [] 
        self.items = [] 
        self.itemDescriptions = [] 
        self.grabbables = []
    # adds an item to the room 
    # the item is a string (e.g., table) 
    # the desc is a string that describes the item (e.g., it is made of wood) 
# getters and setters for the instance variables 
    @property 
    def name(self): 
        return self._name 
 
    @name.setter 
    def name(self, value): 
        self._name = value 
 
    @property 
    def exits(self): 
        return self._exits 
 

    @exits.setter 
    def exits(self, value): 
        self._exits = value 
 

    @property 
    def exitLocations(self): 
        return self._exitLocations 
 

    @exitLocations.setter 
    def exitLocations(self, value): 
        self._exitLocations = value 
 

    @property 
    def items(self): 
        return self._items 
 
    @items.setter 
    def items(self, value): 
        self._items = value 
 

    @property 
    def itemDescriptions(self): 
        return self._itemDescriptions 
 
    @itemDescriptions.setter 
    def itemDescriptions(self, value): 
        self._itemDescriptions = value 
 

    @property 
    def grabbables(self): 
        return self._grabbables 
 

    @grabbables.setter 
    def grabbables(self, value): 
        self._grabbables = value

    # adds an exit to the room 
    # the exit is a string (e.g., north) 
    # the room is an instance of a room 
    def addExit(self, exit, room): 
        # append the exit and room to the appropriate lists 
        self._exits.append(exit) 
        self._exitLocations.append(room)
    
    def addItem(self, item, desc): 
        # append the item and description to the appropriate lists 
        self._items.append(item) 
        self._itemDescriptions.append(desc)
    
        # adds a grabbable item to the room 
        #the item is a string (e.g., key) 
    def addGrabbable(self, item): 
        # append the item to the list 
        self._grabbables.append(item)
    
    # removes a grabbable item from the room 
    # the item is a string (e.g., key)
    def delGrabbable(self,item):
        # remove the item from the list 
        self._grabbables.remove(item)
    # returns a string description of the room 
    def __str__(self): 
        # first, the room name 
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room 
        s += "You see: " 
        for item in self.items: 
            s += item + " " 
        s += "\n" 
        # next, the exits from the room 
        s += "Exits: " 
        for exit in self.exits: 
            s += exit + " " 
        return s

# creates the rooms 

def createRooms(): 
    # r1 through r4 are the four rooms in the mansion 
    # currentRoom is the room the player is currently in (which 
    # can be one of r1 through r4) 
    # since it needs to be changed in the main part of the 
    #  program, it must be global 
    global currentRoom 
 

 # create the rooms and give them meaningful names 
    r1 = Room("Room 1") 
    r2 = Room("Room 2") 
    r3 = Room("Room 3") 
    r4 = Room("Room 4") 
 
    # add exits to room 1 
    r1.addExit("east", r2) 
    r1.addExit("south", r3) 
    # add grabbables to room 1 
    r1.addGrabbable("key") 
    # add items to room 1 
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.") 
    r1.addItem("table", "It is made of oak. A golden key rests  on it.") 
 

    # add exits to room 2 
    r2.addExit("west", r1) 
    r2.addExit("south", r4) 
    # add items to room 2 
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.") 
    r2.addItem("fireplace", "It is full of ashes.") 
 
    # add exits to room 3 
    r3.addExit("north", r1) 
    r3.addExit("east", r4) 
    # add grabbables to room 3 
    r3.addGrabbable("book") 
    # add items to room 3 
    r3.addItem("bookshelves", "They are empty. Go figure.") 
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.") 
    # add exits to room 4 
    r4.addExit("north", r2) 
    r4.addExit("west", r3) 
    r4.addExit("south", None) # DEATH! 
    # add grabbables to room 4 
    r4.addGrabbable("6-pack") 
    # add items to room 4 
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.") 
 

 # set room 1 as the current room at the beginning 
 #  of the game 
 currentRoom = r1 
###################################################### 
# START THE GAME!!! 
inventory = [] # nothing in inventory...yet 
createRooms()  # create the rooms