authors={}
f=open("SciFiLiBooks.txt")
for line in f:
    templine=line.split(',')
    author=templine[1].strip()
    if author not in authors.keys():
        authors[author]=1
    else:
        authors[author]+=1
print(authors)
authornumlist=authors.values()
print(max(authornumlist))