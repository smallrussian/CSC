#French phrase Translator 
#Returns a sorted list of french words, literal translations, and english meanings
#Last Edited: 10/20/2021
#Julian Shniter
class Phrase:
    french=""
    literal=""
    meaning=""

#i spent WAY too long trying to make this more complicated than it needs to be
def readlines(frarr, litarr, meanarr):
    f=open("french_slang.txt", 'r')
    f.readline()
    f.readline()
    f.readline()
    line=3
    while line<=80:
        tempphrase.french=f.readline()
        newtempfrench= tempphrase.french.replace('\n', "")
        frarr.append(newtempfrench)
        line+=1
        templst=f.readline().split("(", 1)
        tempmean1=templst[1].replace(")", "")
        tempmean2=tempmean1.replace("\n", "")
        litarr.append(templst[0])
        meanarr.append(tempmean2)
        line+=1
        f.readline()
        line+=1
        
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def SelectionSort(arr, n):
    for i in range(n):
        min_index=i
        min_str=arr[i]
        for j in range(i+1, n):
            if min_str>arr[j]:
                min_str=arr[j]
                min_index=j
        if min_index!=i:
            temp=arr[i]
            arr[i]=arr[min_index]
            arr[min_index]=temp
    return arr 

def BubbleSort(arr, n):
    for i in range(n):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
        if swapped==False:
            break
    return arr  

#mainloop
tempphrase=Phrase
french=[]
literal=[]
meaning=[]
readlines(french, literal, meaning)
print("The list of french sayings is {}".format(BubbleSort(french, len(french))))
print("The list of literal english translations is {}".format(SelectionSort(literal, len(literal))))
print("The list of english meanings is {}".format(InsertionSort(meaning)))
