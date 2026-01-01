'''
Write a program to fill in a letter template given below with name and date. 
letter =  
Dear <|Name|>, 
You are selected! 
<|Date|
'''

name = input("Enter your name please: ")
date = "1/1/2026"
print(f"Dear {name}, \nYou are selected! \n{date}")

# same code using replace function of string
letter =  "\nDear <|Name|>, \nYou are selected! \n<|Date|"
print(letter.replace("<|Name|>","Srushti").replace("<|Date|", "1 january 2026"))

# output
# Dear Srushti, 
# You are selected! 
# 1 january 2026