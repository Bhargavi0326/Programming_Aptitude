mylist = list(map(int,input().split()))
newlist = []
[newlist.append(x) for x in mylist if x not in newlist]
print (newlist)
