#GCD calculator using Euclids algorithm
#finds the greatest common denominator
#lasted edited: 10/18/2021
#Julian Shniter
def gcd(x,y):
    if y==0:
        return x
    else:
        while y!=0:
            x, y = y, x%y
        return x
#the first one has all the steps written out
#this one knows that all it needs to do is get y to equal zero so it can return x
#it does this by returning the function itslef with the switched values
#therefore it needs to call the function until it gets y to equal zero so it can return x
#hence recursion
def gcd2(x,y):
    if y==0:
        return x
    else:
        return gcd2(y, x%y)
#this one does the same thing except its all compacted into one line 
def gcd3(x,y):
    return x if not y else gcd3(y, x%y)
#go ahead and insert your own numbers to test it 
print(gcd(50,150))
print(gcd2(50,-10))
print(gcd3(50,10))
print(gcd3(50,-10))