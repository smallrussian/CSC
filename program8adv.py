#julian Shniter
#pokemon picker
#selects a pokemon from a file and displays abilities and classification
#last edited 11/15/2021
from sort import BinarySearch
import operator
class Pokemon:
    def __init__(self, abilities, classification, name) -> None:
        self.abilities=abilities
        self.classification=classification
        self.name=name

def find_pokemon(input, array):
    for obj in array:
        if obj.name==input:
            return obj

#and here i thought i was just goijng to be able to import it 
def BinarySearch(arr, low, high, x):
    if high>=low: #lines 58 and 67 feel redundant
        mid=low+(high-low)//2
        if arr[mid].name==x:
            return mid
        elif arr[mid].name>x:
            return(BinarySearch(arr, low, mid-1, x))
        else:
            return(BinarySearch(arr, mid+1, high, x))
    else:
        return -1

#mainloop
objlist=[]
f=open('pokemon.csv', 'r')
f.readline()
for line in f:
    newline=line.replace(',,,', '').replace(',,', ',').replace('\n', '')
    array=newline.split(',')
    objlist.append(Pokemon(array[0], array[1], array[2]))
    if not f.readline():
            break
objlist.sort(key=operator.attrgetter('name'))
while True:
    usrinput=str(input('Please select your Pokemon. \nUse exact spelling and capitlization\nEnter "Q" to quit\n'))
    if usrinput=='Q':
        break
    pokepick=objlist[BinarySearch(objlist, 0, len(objlist), usrinput)]
    print(pokepick.name)
    print('{} is a {}'.format(pokepick.name, pokepick.classification), end="\n")
    abilitystring="Their abilities are "
    if ";" in pokepick.abilities:
        abilitylist=pokepick.abilities.split(';')
        for ability in abilitylist:
            abilitystring+="{}, ".format(ability)
    
    else:
        abilitystring+='{} '.format(pokepick.abilities)
    print(abilitystring.replace("['","").replace("']","").replace("'", ""))
print("Thanks for playing")