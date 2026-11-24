# name=input("Enter your name")
Letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
# print(f" Dear {name} \n you are selected")
print(Letter.replace("<|Name|>","Rabbani").replace("<|Date|>","24 November 2030"))