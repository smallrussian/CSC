from tkinter import *
from PIL import ImageTk, Image
class Room: 

 # the constructor 
    def __init__(self, name, image): 
  # rooms have a name, exits (e.g., south), exit 
  #  locations (e.g., to the south is room n), items 
  #  (e.g., table), item descriptions (for each item), 
  #  and grabbables (things that can be taken into 
  #  inventory) 
        self.name = name 
        self.image = image
        self.exits = []
        self.exitLocations = [] 
        self.items = []
        self.itemDescriptions = {} 
        self.grabbables = []
        self.usables=[]
        self.usableskeys=[]
        self.exitconditions=[]
        self.useableeffects=[]
        self.functionconditions=[]
        self.commandparams=[]
        self.changecommandidentifier=False
        self.exitcommandidentifiers=[]
        self.exitcommands1=[]
        self.exitcommands2=[]
        self.exitcommandparams=[]
        self.exitmessages=[]
        self._inventoryDescriptions={}
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
    #ALL BELOW ARE NEW BUT I DOUBT I WILL USE THEM ALL 
    @property
    def usables(self):
        return(self._usables)
    @usables.setter
    def usables(self, value):
        self._usables=value
    
    @property
    def usableskeys(self):
        return self._usableskeys
    @usableskeys.setter
    def usableskeys(self, value):
        self._usableskeys=value
    @property
    def usableeffects(self):
        return self._useableeffects
    
    @usableeffects.setter
    def useableeffects(self, value):
        self._useableeffects=value    
    

    @property
    def exitconditions(self):
        return self._exitconditions
    
    @exitconditions.setter
    def exitconditions(self, value):
        self._exitconditions=value

    @property
    def functionconditions(self):
        return self._functionconditions

    @functionconditions.setter
    def functionconditions(self, value):
        self._functionconditions=value

    @property
    def commandparams(self):
        return self._commandparams

    @commandparams.setter
    def commandparams(self, value):
        self._commandparams=value

    @property
    def changecommandidentifier(self):
        return self._changecommandidentifier

    @changecommandidentifier.setter
    def changecommandidentifier(self, value):
        self._changecommandidentifier=value
    
    @property
    def exitcommandidentifiers(self):
        return self._exitcommandidentifiers
    
    @exitcommandidentifiers.setter
    def exitcommandidentifiers(self, value):
        self._exitcommandidentifiers=value
    
    @property 
    def exitcommands(self):
        return self._exitcommands
    @exitcommands.setter
    def exitcommands2(self, value):
        self._exitcommands=value

    @property
    def exitcommandparams(self):
        return self._exitcommandparams
    
    @exitcommandparams.setter
    def exitcommandparams(self, value):
        self._exitcommandparams=value
        
   

    @property
    def exitmessasges(self):
        return self._exitmessasges
    
    @exitmessasges.setter
    def exitmessasges(self, value):
        self._exitmessasges=value

    @property
    def inventoryDescriptions(self):
        return self._inventoryDescriptions
    
    @inventoryDescriptions.setter
    def inventoryDescriptions(self, value):
        self._inventoryDescriptions=value

    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image=value

    # adds an exit to the room 
    # the exit is a string (e.g., north) 
    # the room is an instance of a room 
    def addExit(self, exit, room, locked,commands, commandidentifier, *commandparams): 
        # append the exit and room to the appropriate lists 
        self._exits.append(exit)
        self._exitLocations.append(room)
        self._exitconditions.append(locked)
        self._exitcommands.append(commands)
        self._exitcommandidentifiers.append(commandidentifier)
        self._exitcommandparams.append(commandparams)

    #CHANGES THAT DOOR
    def changeExit(self, room, direction, ):
        for i in range(len(self._exits)):
            if self._exits[i]==direction:
                self._exits[i]=room
    #UNLOCKS DOORS
    def ChangeExitCondition(self, exit):
        for i in range(len(self._exits)):
            if exit==self._exits[i]:
                if self._exitconditions[i]==True:
                    self._exitconditions[i]=False
                else:
                    self._exitconditions[i]=True
    
    def addItem(self, item, desc): 
        # append the item and description to the appropriate lists 
        self._items.append(item) 
        self._itemDescriptions.update({item:desc})
        

    def changeItem(self, item, desc, command, *commandparam):

        self._itemDescriptions[item]=desc
        if self.changecommandidentifier==True:
            command(*commandparam)
            self._changecommandidentifier=False
    
        # adds a grabbable item to the room 
        #the item is a string (e.g., key) 
    def addGrabbable(self, item, desc): 
        # append the item to the list 
        self._grabbables.append(item)
        self._inventoryDescriptions.update({item:desc})
    
    # removes a grabbable item from the room 
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list 
        self._grabbables.remove(item)
    
    #ADDS A USABLE ITEM TO THE ROOM
    def addUsable(self, item):
        #APPENDS USABLE ITEM TO LIST 
        self._usables.append(item)

    #REMOVES A USABLE ITEM FROM THE LIST
    def delUsable(self, item):
        #USED WHEN EXITING A ROOM
        self._usables.remove(item)
    
    #ADDS THE KEY SYSTEM FOR THE USABLES
    def addKey(self, unlock, unlockeffect, *commandparam):
        self._usableskeys.append(unlock)
        self._useableeffects.append(unlockeffect)
        self._commandparams.append(commandparam)
    
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

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
    
    def createRooms(self): 
    # r1 through r4 are the four rooms in the mansion 
    # currentRoom is the room the player is currently in (which 
    # can be one of r1 through r4) 
    # since it needs to be changed in the main part of the 
    #  program, it must be global 
    
        Game.rooms=[]
 

 # create the rooms and give them meaningful names 
        r1 = Room("Room 1", 'r1.gif') 
        r2 = Room("Room 2", 'r2.gif') 
        r3 = Room("Room 3", 'r3.gif') 
        r4 = Room("Room 4", 'r4.gif') 
        r5 = Room("Room 5", 'r4.gif')
        r6 = Room("Room 6", 'r4.gif')
        r7 = Room("win room ",'r4.gif')
        # add exits to room 1 
        r1.addExit("east", r2, False, None, False, None)
        r1.addExit("south", r3, False, None, False, None) 
        r1.addExit("up", r6, True, None, False, None)
   
    
    # add grabbables to room 1 
        r1.addGrabbable("sword", 'the blade inscription says "Storm Ruler"')
    # add items to room 1 
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.") 
   
        r1.addItem("campfire", "There seems to be some kind of sword sticking out of it. \nIs it useable?")
        r1.addUsable("old_key")
        r1.addKey("You open the door", r1.ChangeExitCondition, "up")
        Game.rooms.append(r1)
 
    # add exits to room 2 
        r2.addExit("west", r1, False, None, False,  None) 
        r2.addExit("south", r4, False, None, False, None) 
    # add items to room 2 
        r2.addItem("table", "It is made of oak. A note and a key rest on it.") 
        r2.addItem("rug", "It is nice and Armenian. It also needs to be vacuumed.") 
        r2.addItem("fireplace", "It is full of ashes.") 
    #add grabables to room 2
        r2.addGrabbable("key", "a key used to open a chest")
        r2.addGrabbable("note" , "It says 'Your task is to find and kill the Giant Yhorm") 
        Game.rooms.append(r2)
 
    # add exits to room 3 
        r3.addExit("north", r1, False, None, False, None)
        r3.addExit("east", r4, False, None, False, None) 
        r3.addExit("west", r5, False, None, False, None)
        # add grabbables to room 3 
        #r3.addGrabbable("book", "the sword kills giants") 
        # add items to room 3 
    
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("television", 'The TV is extremely faint and low resolution, you can just barley make out some\nbald man saying "Id rather die as the man I was than live the life I just saw!')
        r3.addItem("sign", "it says: NO ESCAPE")
        r3.addItem("wall", "It has blood written on it: Wake the giant up so he can have a tasty snack")
        Game.rooms.append(r3)
        # add exits to room 4 
        r4.addExit("north", r2, False, None, False, None) 
        r4.addExit("west", r3, False, None, False, None) 
         # DEATH! 
        # add grabbables to room 4 
        r4.addGrabbable("6-pack", "its a bunch of beer") 
        # add items to room 4 
        r4.addItem("bookshelves", "They are empty. Go figure.") 
        r4.addItem("brew_rig", "Stolen from an Anhueiser-Busch Brewery in St. Louis. A 6-pack is resting beside it.") 
        r4.addItem("chest", "A chest that is locked tight")
        r4.addUsable("key")
        r4.changecommandidentifier=True
        r4.addKey("You open the chest and unlock it", r4.changeItem, "chest", "An open chest with a book inside", r4.addGrabbable, "book", "Storm Ruler: Greatsword with a broken blade, also known as the Giantslayer for the residual strength of storm that brings giants to their knees.\nYhorm the Giant once held two of these, but gave one to the humans that doubted him, and left the other to a dear friend before facing his fate as a Lord of Cinder.")
        # THIS IS ROOM 5, DOESNT HAVE TOO MUCH IN IT 
        Game.rooms.append(r4)
        r5.addExit("east", r3, False, None, False, None)
        r5.addItem("hook", "a small command hook on a wall. An old_key rests on it ")
        r5.addGrabbable("old_key", "a key used to unlock an unknown door")
        #ROOM 6 IS THE ONE WITH THE GIANT 
        Game.rooms.append(r5)
        r6.addExit("south", None, False, None, False, None)
        r6.changecommandidentifier=True
        r6.addItem("giant", "A large sleeping giant named Yhorm")
        r6.addUsable("sword")
        r6.addKey("You hear the giant's death curtle", r4.changeItem, "giant", "A dead giant", r6.changeExit, r7, "south")
        Game.rooms.append(r6)
        #THIS IS THE WIN ROOM
       
        r7.addItem("poster", "You win, BUT THERE IS NO ESCAPE")
        Game.rooms.append(r7)
    # set room 1 as the current room at the beginning 
        Game.currentRoom=r1
        Game.inventory=[]
    #  of the game 

# sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process()
        # bind the Tab key to the function complete()
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
    
# set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):# if dead, set the skull image
            Game.img = PhotoImage(file="death.gif")
        else:# otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
            # display the image on the left of the GUI
            Game.image.config(image=Game.img)
            Game.image.image = Game.img
    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):# if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing ""you can do now\nis quit.\n")
        else:# otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}""\n\n".format(status, Game.currentRoom, Game.inventory))
            Game.text.config(state=DISABLED)
            # support for tab completion
            # add the words to support
            if (Game.currentRoom != None):
                Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables
    
    def play(self):
        #create the room instances
        self.createRooms()
        #configure the Gui
        self.setupGUI()
        #set the current room
        self.setRoomImage()
        #set the initial status
        self.setStatus("WELCOME TO ROOM ADVENTURE")
    
    def process(self, event):
        #prompt for player input
     # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, and take
        # valid nouns depend on the verb
        action = Game.player.input.get()
    # set the user's input to lowercase to make it easier to
    # compare the verb and noun to known values
        action = action.lower().strip()
    # exit the game if the player wants to leave (supports
    # quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)
        
        if(Game.currentRoom==None):
            #clears the players input
            Game.player_input.delete(0, END)
            return
    # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

    # the game only understands two word inputs
        if (len(words) == 2):
        # isolate the verb and noun
            verb = words[0]
            noun = words[1]

        # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                # check for valid exits in the current room
                for i in range(len(Game.currentRoom.exits)):
                    # a valid exit is found
                    if (noun == Game.currentRoom.exits[i]):
                        if Game.currentRoom.exitconditions[i]==True:
                            #I PUT IN LOCKED DOORS 
                            response="This door is locked"
                            break
                    # change the current room to the one that is
                    # associated with the specified exit
                #HERE IS THE SKELETON OF ME TRYING TO GET DOORS TO LOCK WHEN YOU LEAVE A ROOM BUT I DIDNT HAVE TIME
                        if Game.currentRoom.exitcommandidentifiers[i]==True:
                            Game.currentRoom.exitcommands[i](Game.currentRoom.exitcommandparams[i])
                            Game.currentRoom.exitcommands[i](Game.currentRoom.exitcommandparams[i])
                        Game.currentRoom = Game.currentRoom.exitLocations[i]
                    

                        # set the response (success)
                        response = "Room changed."
                        # no need to check any more exits
                        break
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                for i in range(len(Game.currentRoom.items)):
                    # a valid item is found

                    if (noun == Game.currentRoom.items[i]):
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[noun]
                        # no need to check any more items
                        break
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is foundta
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(noun)
                        Game.inventorydesc.update({grabbable:Game.currentRoom.inventoryDescriptions[noun]})
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable) 
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break
            #THIS WAS VERY TRICKY TO GET BUT I MANAGED IT 
            elif (verb=="use"):
                #SETS THE DEFAULT RESPONSE
                if noun not in Game.inventory:
                    print("You don't have that item")
                reponse="You can't use that" 
                for i in range(len(Game.currentRoom.usables)):
                    if noun==Game.currentRoom.usables[i]:
                        response=Game.currentRoom.usableskeys[i]
                        #print(currentRoom.commandparams[i])
                        #TAKES COMMAND FROM PARAMTERS AND EXCUTES USING THOSE PARAMAGERS
                        Game.currentRoom.useableeffects[i](*Game.currentRoom.commandparams[i])
                        Game.inventory.remove(noun)
                        Game.inventorydesc.pop(noun)

            elif verb=="view":
                #A SIMPLE INVENTORY FUNCTION
                if noun not in Game.inventory:
                    response="You don't have that item"
                else:
                    response=Game.inventorydesc[noun]


    
######################################################
# START THE GAME!!!
# we'll put the commands in an array
VERBS = [ "go", "look", "take" ]
QUIT_COMMANDS = [ "exit", "quit", "bye" ]
# window size
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
