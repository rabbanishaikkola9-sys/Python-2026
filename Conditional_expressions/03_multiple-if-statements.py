name=input("Enter your name :")
a=int(input("Eneter your age:"))
# If elif and else statements

# If statement no :1
if(a%2==0):
    print(f"{a} is even ")
else:
    print(f"{a} is odd ")
    # end of if statement no :1

# If statement no :2
if(a>=18):
    print(f"Hello {name} and Your age is {a} you are eligible to vote") #consent age 
    print("Good for you")
#start of the elif statement of if statement no:2
elif(a<0 or a>120):
    print(f"Your name is {name} and You are entering wrong age {a}")
elif(a==0):
    print(f" our name is {name} and You are entering zero {a} which is not not valid ")
else:
    print(f"Your name is {name} and Your age is {a} you are not  eligible to vote")
    # end of if statement no :2
print("End of the program!!")
