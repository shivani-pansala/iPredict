import re
def validate_password(password):
    if not password[0].isalpha():
        return "Password must start with a letter"
    
    if len(password) < 6 or len(password) > 12:
        return "Password must be between 6 and 12 characters"
   
    if ' ' in password:
        return "Password must not contain spaces"
    
    if not re.search(r'[a-z]', password):
        return "Password must at least one lowercase letter"
    
    if not re.search(r'[A-Z]', password):
        return "Password must at least one uppercase letter"
    
    if not re.search(r'[0-9]', password):
        return "Password must at least one number"
    
    if not re.search(r'[$#@]', password):
        return "Password must at least one special character ($, #, @)"
    
    return password

username = input("Enter your username :")
print(username)
password = input("Enter a password : ")
print(validate_password(password))

'''Output
Enter a password: Abc2@3  
Password is valid

Enter a password:Acdc de
Password must not contain spaces

Enter a password: Avcdd3 
Password must at least one special character ($, #, @)

'''