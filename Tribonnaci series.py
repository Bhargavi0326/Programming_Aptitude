n= int(input())
sum=0
li=[]
for i in range(n):
    if(i==0):
        li.append(0)
    elif(i==1):
        li.append(1)
    else:
        sum=sum+li[i-1]+li[i-2]
        li.append(sum)
        sum=li[i-2]
print(li)
        
