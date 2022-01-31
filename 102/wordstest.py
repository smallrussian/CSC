from words import Word
from location import Location
l1 = Location(3, 5)
w1 = Word("zebra", "HR", l1)
l2 = Location(-10, 10)
w2 = Word("Panther", "DLD", l2)
l3 = Location()
w3 = Word("GIRAFFE", "DRU", l3)
print(w1)
print(w2)
print(w3)