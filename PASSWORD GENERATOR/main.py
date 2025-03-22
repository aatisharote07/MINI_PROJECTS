import random 
import string
def generate_password():
    length=int(input("Enter the desired password length: ").strip())
    include_uppercase=input("Include uppercase letters?(yes/no): ").strip().lower()
    include_special=input("Include Special Characters?(yes/no): ").strip().lower()
    include_digits=input("Include Digits?(yes/no): ").strip().lower()

    if length<4:
        print("Password must be atleast 4 characters.")
        return None
    lower = string.ascii_lowercase
    uppercase=string.ascii_uppercase if include_uppercase== "yes" else ""
    special=string.punctuation if include_special== "yes" else ""
    digit=string.digits if include_digits== "yes" else ""

    all_characters= lower + uppercase + special + digit 

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))    
    if include_special == "yes":
        required_characters.append(random.choice(special))    
    if include_digits == "yes":
        required_characters.append(random.choice(digit))    
    remaining_length = length - len(required_characters)
    password= required_characters
    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)

    random.shuffle(password)    
    str_password="".join(password)  
    return str_password  
password = generate_password()
if password:  
    print("Generated Password:",password)  