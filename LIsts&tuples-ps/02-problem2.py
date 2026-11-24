marks=[]
marks1=int(input("Enter the marks here: "))
marks.append(marks1)
marks2=int(input("Enter the marks here: "))
marks.append(marks2)
marks3=int(input("Enter the marks here: "))
marks.append(marks3)
marks4=int(input("Enter the marks here: "))
marks.append(marks4)
marks5=int(input("Enter the marks here: "))
marks.append(marks5)
marks6=int(input("Enter the marks here: "))
marks.append(marks6)
marks.sort()
print(f"In the sorted manner {marks}") # from small to big 
print(f" The original mark list is :{marks}")
marks.sort(reverse=True) # from big to small 
print(f"In the sorted manner {marks}")