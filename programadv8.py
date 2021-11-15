from os import name
from sort import BinarySearch
from functools import reduce
class Pokemon:
    def __init__(self, abilities, classification, name) -> None:
        self.abilities=abilities
        self.classification=classification
        self.name=name

def read_csv():
    
    s=f.readline().replace(',,,', '').replace(',,', ',').replace('\n', '')
    array=s.split(',')
    return array

#mainloop
objlist=[]
f=open('pokemon.csv', 'r')
f.readline()
for line in f:
    newline=line.replace(',,,', '').replace(',,', ',').replace('\n', '')
    array=newline.split(',')
    objlist.append(Pokemon(array[0], array[1], array[2]))
    if f.readline()=='':
            break
print(objlist)
print(objlist[1].name)