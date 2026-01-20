num = int(input("Enter a number: "))
even=odd=zero=0
while num>0:
    digit=num%10
    if digit==0:
        zero=zero+1
    elif digit%2==0:
        even=even+1
    else:
        odd=odd+1
    num=num//10
print("Even digits:", even)
print("Odd digits:", odd)  
print("Zero digits:", zero) 