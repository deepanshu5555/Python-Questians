import random
import math
print("Welcome to the number guessing game! Enter any number between 330 to 430")
x=random.randint(330,430)
n=int(math.log((430-330),2))+1
print("You only have ",n," attamps")
flag=False
while(n):
    print("Enter Your number")
    a=int(input())
    if(a==x):
        print("Yeah! You identified the number")
        flag=True
        break
    elif(a>x):
        if(n!=1):
            print("Please try again! The number you guessed is too high")
    else:
        if(n!=1):
            print("Please try again! The number you guessed is too small")
    n=n-1
if(flag is False):
    print("Oops! All you chances are finished. Better luck next time!")
print("The number was ",x)
    
    
                
                
            
    
    
        
