def divisible_not(num1,num2):
    if(num1%num2 == 0):
        return "Diviible"
    else:
        return "Not Divisible"

a=int(input())
b=int(input())
print(divisible_not(a,b))
