import random
# all list
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@']

# user input
in_letter = int(input("Enter how many letters you want:"))
in_num = int(input("Enter how many number you want:"))
in_symbol = int(input("Enter how many symbol you want:"))

# main logic

list_password =[]

for char in range(1 , in_letter+1):
    list_password += random.choice(letter)
    
for num in range(1 , in_num+1):
    list_password += random.choice(number)
    
for sym in range(1 , in_symbol+1):
    list_password += random.choice(symbol)

random.shuffle(list_password)

password =""
for char in list_password:
    password += char

print(f"Genareted password is: {password}")   
