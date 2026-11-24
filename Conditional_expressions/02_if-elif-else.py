name=input("Enter your name :")
a=int(input("Enter your age:"))
# If else statement 
if(a>=18):
    print(f"Hello {name} and Your age is {a} you are eligible to vote") #consent age 
    print("Good for you")
elif(a<0 or a>120):
    print(f"Your name is {name} and You are entering wrong age {a}")
elif(a==0):
    print(f" our name is {name} and You are entering zero {a} which is not not valid ")
else:
    print(f"Your name is {name} and Your age is {a} you are not  eligible to vote")
print("End of the program!!")
