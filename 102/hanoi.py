def Towers(i):
    if i<=2:
        return 1
    else:
        return(Towers(i-1)*2+1)

def earnings(i):
    if i<=1:
        return 60000
    else:
        return(earnings(i-1)*1.03)

def enrollment(i):
    if i<=0:
        return 14286
    else:
        return(enrollment(i-1)*.88)
print(enrollment(5))
