from tkinter import *
from Room import Room

################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)
    # creates the rooms
    def createRooms(self):
            Game.rooms = []
            # create the rooms and give them meaningful names
            r1 = Room("Room 1", "r1.gif")
            r2 = Room("Room 2", "r2.gif")
            r3 = Room("Room 3", "r3.gif")
            r4 = Room("Room 4", "r4.gif")
            # add exits to room 1
            r1.addExit("east", r2)
            r1.addExit("south", r3)
            # add grabbables to room 1
            r1.addGrabbable("key")
            # add items to room 1
            r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
            r1.addItem("table", "It is made of oak. A golden key rests on it.")
            Game.rooms.append(r1)
            # add exits to room 2
            r2.addExit("west", r1)
            r2.addExit("south", r4)
            # add items to room 2
            r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
            r2.addItem("fireplace", "It is full of ashes.")
            Game.rooms.append(r2)
            # add exits to room 3
            r3.addExit("north", r1)
            r3.addExit("east", r4)
            # add grabbables to room 3
            r3.addGrabbable("book")
            # add items to room 3
            r3.addItem("bookshelves", "They are empty. Go figure.")
            r3.addItem("statue", "There is nothing special about it.")
            r3.addItem("desk", "The statue is resting on it. So is a book.")
            Game.rooms.append(r3)
            # add exits to room 4
            r4.addExit("north", r2)
            r4.addExit("west", r3)
            r4.addExit("south", None) # DEATH!
            # add grabbables to room 4
            r4.addGrabbable("6-pack")
            # add items to room 4
            r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
            Game.rooms.append(r4)
            # set room 1 as the current room at the beginning of the game
            Game.currentRoom = r1
            Game.inventory = []

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
    # play the game
    def play(self):
            # create the room instances
            self.createRooms()
            # configure the GUI
            self.setupGUI()
            # set the current room
            self.setRoomImage()
            # set the initial status
            self.setStatus("WELCOME TO ROOM ADVENTURE!")
    # processes the player's input
    def process(self, event):
            # grab the player's input from the Entry widget
            action = Game.player_input.get()
            # set the user's input to lowercase
            action = action.lower().strip()
            # exit the game if the player wants to leave
            if (action in QUIT_COMMANDS):
                exit(0)
            # if the current room is None, then the player is dead
            # this only happens if the player goes south when in room 4
            if (Game.currentRoom == None):
                # clear the player's input
                Game.player_input.delete(0, END)
                return
            # set a default response
            response = "I don't understand. Try verb noun. Valid " "verbs\nare {}.".format(", ".join(VERBS))
            # split the user input into words (words are separated by spaces)
            # and store the words in a list
            words = action.split()
            # the game only understands two word inputs
            if (len(words) == 2):
                # isolate the verb and noun
                verb = words[0].strip()
                noun = words[1].strip()
                # we need a valid verb
                if (verb in VERBS):
                    # the verb is: go.
                    if (verb == "go"):
                        # set a default response
                        response = "You can't go in that direction."
                        # check if the noun is a valid exit
                        if (noun in Game.currentRoom.exits):
                            # get its index
                            i = Game.currentRoom.exits.index(noun)
                            # change the current room to the one
                            # that is associated with the specified
                            # exit
                            Game.currentRoom =Game.currentRoom.exitLocations[i]
                            # set the response (success)
                            response = "You walk {} and enter ""another room.".format(noun)
                    # the verb is: look
                    elif (verb == "look"):
                            # set a default response
                            response = "You don't see that item."
                            # check if the noun is a valid item
                            if (noun in Game.currentRoom.items):
                                # get its index
                                i = Game.currentRoom.items.index(noun)
                                # set the response to the item's description
                                response = Game.currentRoom.itemDescriptions[i]
                    # the verb is: take
                    elif (verb == "take"):
                            # set a default response
                            response = "You don't see that item."
                            # check if the noun is a valid grabbable and
                            # is also not already in inventory
                            if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                                # get its index
                                i = Game.currentRoom.grabbables.index(noun)
                                # add the grabbable item to the player's inventory
                                Game.inventory.append(Game.currentRoom.grabbables[i])
                                # set the response (success)
                                response = "You take {}.".format(noun)
            # display the response on the right of the GUI
            # display the room's image on the left of the GUI
            # clear the player's input
            self.setStatus(response)
            self.setRoomImage()
            Game.player_input.delete(0, END)
                            

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