import re #Regex


#Length Check 
def check_length(password):
    length = len(password)
    if length >= 20:
        return 4              #excellent, especially for important accounts
    elif length >= 16:
        return 3              #very strong
    elif length >= 12:
        return 2              #strong
    elif length >= 8:
        return 1              #good 
    else:
        return 0              #Too short 
    
#Uppercase check 
def check_uppercase(password):
    return 1 if re.search(r'[A-Z]', password) else 0

#Lowercase check
def check_lowercase(password):
    return 1 if re.search(r'[a-z]', password) else 0

#digit check 
def check_digit(password):
    return 1 if re.search(r'\d', password) else 0

#Special character check
def check_special_char(password):
    return 1 if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) else 0

#repeeated characters check 
def check_repeated_char(password):
    return -1 if re.search(r'(.)\1\1', password) else 0

#common sequeneces check
def check_sequential(password):
    sequences = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 
                 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop',
                 '123', '234', '345', '456', '567', '678', '789']
    password_lower = password.lower()
    for seq in sequences:
        if seq in password_lower:
            return -1
    return 0

#anlyzing password 
def analyze_password(password):
    results = {
        'common_password': check_common_password(password),
        'length' : check_length(password),
        'uppercase' : check_uppercase(password),
        'lowercase' : check_lowercase(password),
        'digit' : check_digit(password),
        'special_char' : check_special_char(password),
        'repeated_char' : check_repeated_char(password),
        'sequential' : check_sequential(password), 
    }
    return results

from common_passwords import load_common_passwords, is_common_password

COMMON_PASSWORDS = load_common_passwords()

def check_common_password(password):
    return -2 if is_common_password(password, COMMON_PASSWORDS) else 0


"""if __name__ == "__main__":
    test = "Hello@123"
    print(analyze_password(test))"""