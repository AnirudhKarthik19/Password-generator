import random
import string
import secrets
import zxcvbn
# Function to Generate Username        
def generate_username():
    # Get user input for name and website/application name
    username = input("Enter Your Name").lower()
    site = input("Enter the name of website/Application:").lower()

    # Generate a random number between 100 and 999

    random_number = random.randint(100,999)

    # Generate a random string of 3 characters
    
    final_username= username[:5]+site[:3]+str(random_number)
    return final_username 

# Function to Generate Password
def generate_password(length=16):
    allowed_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += secrets.choice(allowed_characters)
    return password
# Function to Check Password Strength
# def password_strength(password):
#     score =0
#     if len(password) >= 8:
#         score += 1
#     if any(char.islower() for char in password):
#         score += 1
#     if any(char.isupper() for char in password):
#         score += 1
#     if any(char.isdigit() for char in password):
#         score += 1
#     if any(char in string.punctuation for char in password):
#         score += 1
#     if score <= 2:
#         return "Weak"
#     elif score == 3:
#         return "Moderate"
#     else:
#         return "Strong"
 
def password_strength(password):
    result= zxcvbn.zxcvbn(password)
    score = result['score']
    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    else:
        return "Strong"



# Call the function and print the generated username
generated_username = generate_username()
print("Generated Username:", generated_username)

# Call the function and print the generated password
generated_password = generate_password()
print("Generated Password:", generated_password)

# Check the strength of the generated password
strength = password_strength(generated_password)  
print("Password Strength:", strength)      
