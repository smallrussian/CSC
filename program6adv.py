import BarChart as bc
import operator
class ValueStorage:
    title=''
    x_axis=''
    source=''
    counter=''

def readanddict(dict):
    templist=f.readline().split(',')
    if len(templist)==5:
        dict[templist[1]]=int(templist[3])
        vals.counter=templist[0]
    return dict

def drawchart(num, counter, dict):
    # create the bar chart
    title = ValueStorage.title
    x_axis = ValueStorage.x_axis
    source = ValueStorage.source
    chart = bc.BarChart(title, x_axis, source)
    
    # add the bars and caption to the bar chart
    keycounter=0
    for j in range(len(dict)):
        key,val=dict[j]
        chart.add(key,val,key)
        keycounter+=1
        if keycounter==num:
            break

    #chart.add('Delhi',       27890, 'South Asia')
    #chart.add('Shanghai',    25779, 'East Asia')
    #chart.add('Beijing',     22674, 'East Asia')
    #chart.add('Mumbai',      22120, 'South Asia')
    #chart.add('São Paulo',   21698, 'Latin America')
    #chart.add('Mexico City', 21520, 'Latin America')
    #chart.add('Osaka',       20409, 'East Asia')
    #chart.add('Cairo',       19850, 'Middle East')
    #chart.add('Dhaka',       19633, 'South Asia')
    chart.set_caption(counter)

    # draw the bar chart
    chart.draw()
    chart.save('test.png')
    chart.save('test.pdf')
    #chart.leave_window_open()
    return chart

#mainloop

vals=ValueStorage
colorlist=[]
unsorteddict={}
filenameinput='cities.txt'
#filenameinput=str(input("Please enter a filename\n"))
barcount=int(input("How many bars do you want to display?\n"))
f=open(filenameinput, 'r')
ValueStorage.title=f.readline()
ValueStorage.x_axis=f.readline()
ValueStorage.source=f.readline()
f.readline()
while True:
    numberstr=f.readline()
    #print(numberstr)
    numberstr.replace('\n', '')
    number=int(numberstr)
    for i in range(number):
        readanddict(unsorteddict)
    cd = sorted(unsorteddict.items(),key=operator.itemgetter(1),reverse=True)
    #one of these answers taught me how to do this 
    #https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
    drawchart(barcount, ValueStorage.counter, cd)
        #pass
    #f.readline
    if not f.readline():
        break


#sorted_d = dict( sorted(unsorteddict.items(), key=operator.itemgetter(1),reverse=True)) #i wanted to sort the values in descending order
#credit to https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php for teaching me to do this
print(type(unsorteddict['Black Panther']))