###############################################################################
# Word Search (Grid class)
# Dr. Jean Gourd
# Last modified on 2020-11-05
#
# A partially implemented Grid class for the programming assignment Word
#  Search (part 2).
# Requires Location.py and Word.py.
###############################################################################

# import libraries
from Location import Location
from Word import Word
from random import randint

# the Grid class
# a Grid has a size (the same for both width and height), a grid of letters, and Word instances that are within the Grid
class Grid:
    # class variables
    # the character representing a "blank" letter in the grid
    BLANK = "."
    # the max number of tries to position a word
    MAX_TRIES = 1000

    # the constructor
    # **implement the constructor here**
    def __init__(self, size=25):
    
        self._size=size
        # initialize the grid
        self._grid=grid
        # add the rows
            # create a new blank row

            # fill it with spaces

            # add the new row

        # initialize the words
        self._words=words

    # getters and setters
    ## I like putting them together - Julian
    @property
    def grid(self):
        return self._grid
    @grid.setter
    def grid(self, value):
        self._grid=value
    
    @property
    def words(self):
        return self._words
    @words.setter
    def words(self, value):
        self._words=value


    # tries to position a word at the specified orientation in the grid
    def position(self, word, orientation):
        # set the default min and max row and col
        min_row = 0
        max_row = self._size - 1
        min_col = 0
        max_col = self._size - 1

        # tweak the max_col value based on the HR orientation
        # **modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)**
        max_col = self._size - len(word)

        # create the Word instance
        word = Word(word, orientation)

        # select a random location based on the min and max values
        loc = Location(randint(min_row, max_row), randint(min_col, max_col))
        # check if this location works up to the specified maximum number of tries
        tries = 0
        while (not self._check(word, loc)):
            # stop trying if we've reached the specified maximum number of tries
            if (tries == Grid.MAX_TRIES):
                return
            # select a new random location
            loc = Location(randint(min_row, max_row), randint(min_col, max_col))
            # note the attempt
            tries += 1
        # update the word's location
        word.location = loc
        # position the word in the grid at the location
        self._position(word)
        # and add it to the list of words
        self._words.append(word)

    # checks if a word can be positioned as specified
    def _check(self, word, loc):
        # the starting row and col for the word
        row = loc.row
        col = loc.col

        # check if the word fits for the specified orientation
        for letter in word.word:
            # abort if we don't encounter a space or the appropriate letter
            if (not self._grid[row][col] in [ Grid.BLANK, letter ]):
                return False
            # change the col (based on the HR orientation)
            # **modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)**
            col += 1

        # otherwise, all the letters fit!
        return True

    # positions a word as specified
    def _position(self, word):
        # the starting row and col for the word
        row = word.location.row
        col = word.location.col

        # position the word
        for letter in word.word:
            # place the current letter
            self._grid[row][col] = letter
            # change the col (based on the HR orientation)
            # **modify to support remaining orientations (HL, VD, VU, DRD, DRU, DLD, DLU)**
            col += 1

    # prints the words
    def print_words(self):
        # **add sorting the words first**
        for word in self._words:
            print(word)

    # prints the solution
    def print_solution(self):
        print(self.__str__(False))

    # return a string representation of the grid
    def __str__(self, fill=True):
        grid = ""
        for row in range(self._size):
            for col in range(self._size):
                # if no letter exists at row,col
                if (self._grid[row][col] == Grid.BLANK and fill):
                    # add a random one
                    grid += "{:2}".format(chr(randint(65, 90)))
                else:
                    grid += "{:2}".format(self._grid[row][col])
            grid += "\n"
        # remove the trailing newline
        grid = grid.rstrip("\n")

        return grid
