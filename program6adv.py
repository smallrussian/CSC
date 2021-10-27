import BarChart as bc
import operator
unsorteddict={}
filenameinput=str(input("Please enter a filename\n"))
barcount=int(input("How many bars do you want to display?\n"))
f=open(filenameinput, 'r')
def readanddict():
    templist=f.readline().split(',')
    if len(templist)==5:
        unsorteddict[templist[1]]=int(templist[3])
    return unsorteddict
def drawchart(num, file):
    # create the bar chart
    if file=="infinity-war.txt":
        title="The {} characters in Avengers Infinity War with the most screentime"
        
    title = 'The 10 most populous cities'
    x_axis = 'Population (thousands)'
    source = 'Source: United Nations'
    chart = BarChart(title, x_axis, source)

    # add the bars and caption to the bar chart
    chart.add('Tokyo',       38194, 'East Asia')
    chart.add('Delhi',       27890, 'South Asia')
    chart.add('Shanghai',    25779, 'East Asia')
    #chart.add('Beijing',     22674, 'East Asia')
    chart.add('Mumbai',      22120, 'South Asia')
    chart.add('São Paulo',   21698, 'Latin America')
    chart.add('Mexico City', 21520, 'Latin America')
    chart.add('Osaka',       20409, 'East Asia')
    chart.add('Cairo',       19850, 'Middle East')
    chart.add('Dhaka',       19633, 'South Asia')
    chart.set_caption('2018')

    # draw the bar chart
    chart.draw()
    chart.save('test.png')
    chart.save('test.pdf')
    chart.leave_window_open()


f.readline()#skip header
f.readline()#more skipping header
f.readline()#more skipping header
f.readline()
while True:
    numberstr=f.readline()
    numberstr.replace('\n', '')
    number=int(numberstr)
    for i in range(number):
        readanddict()
    f.readline
    if not f.readline():
        break
print(unsorteddict)
#keylist=avengersdict.keys()
sorted_d = dict( sorted(unsorteddict.items(), key=operator.itemgetter(1),reverse=True)) #i wanted to sort the values in descending order
#credit to https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php for teaching me to do this
print(len(sorted_d))