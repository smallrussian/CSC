import BarChart as bc
from time import sleep
import operator
from itertools import count
class ValueStorage:
    title=''
    x_axis=''
    source=''
    counter=''
    catdict=dict()

def readanddict(dict):
    templist=f.readline().split(',')
    if len(templist)==5:
        dict[templist[1]]=(int(templist[3]))
        vals.catdict[templist[1]]=templist[4].replace('\n','')
        vals.counter=templist[0]
    return dict
      
def drawchart(num, counter, dict, valclass):
    #reset it so its not broken 
    chart.reset()
    # add the bars and caption to the bar chart
    #if 
    keycounter=0
    for key, val in dict:
        chart.add(key,val, valclass.catdict[key])
        keycounter+=1
        if keycounter==num:
            break
    chart.set_caption(counter)
    # draw the bar chart
    chart.draw()
    chart.save('test.png')
    chart.save('test.pdf')
    #chart.leave_window_open()
    return chart

#mainloop
run_once=0
keybool=True
vals=ValueStorage
colorlist=[]
unsorteddict={}
#filenameinput='game-of-thrones.txt'
print("Please enter a file name\nThe choices are...")
print('"cities.txt"\n"football.txt"\n"countries.txt"\n"brands.txt"\n"cities-usa.txt"\n"movies.txt"\n"baby-names.txt"\n"game-of-thrones.txt"\n"endgame.txt"\n"infinity-war.txt"\n"trademarks.txt"\n"patents.txt"')
while True:
    filenameinput=str(input("Please enter a filename exactly as listed\n"))
    if filenameinput=="cities.txt" or "football.txt"or "brands.txt" or "cities-usa.txt" or "movies.txt" or "baby-names.txt" or "game-of-thrones.txt" or "endgame.txt" or "infinity-war.txt" or "trademarks.txt" or "patents.txt":
        break
    else:
        print("You did not select the correct file, please try again")
barcount=int(input("How many bars do you want to display?\n"))
f=open(filenameinput, 'r')
title=ValueStorage.title=f.readline()
x_axis=ValueStorage.x_axis=f.readline()
source=ValueStorage.source=f.readline()
chart = bc.BarChart(title, x_axis, source)
f.readline()
permcats=list()
randkey=1
while True:
    numberstr=f.readline()
    #print(numberstr)
    numberstr.replace('\n', '')
    number=int(numberstr)
    for i in range(number):
        readanddict(unsorteddict)
    #turn into a tuple so it can be sorted
    decsendingtuple = sorted(unsorteddict.items(),key=operator.itemgetter(1),reverse=True)
    convertdict=dict()#turn the tuple back into a dictionary 
    decsendingdict=dict(decsendingtuple)
    #print(decsendingdict)
    #for f,w in decsendingtuple:
        #for w in range(len(decsendingtuple)):
         #   vals.
    #https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
   
    drawchart( barcount, ValueStorage.counter, decsendingtuple, vals)
    sleep(.1)#i dont really see the need for this because on a slower computer the cpu does this itself
            #due to the time that it takes to think
            
    if not f.readline():
        break

#(a+b)*(c+d)

#sorted_d = dict( sorted(unsorteddict.items(), key=operator.itemgetter(1),reverse=True)) #i wanted to sort the values in descending order
#credit to https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php for teaching me to do this