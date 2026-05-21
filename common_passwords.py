import os

def load_common_passwords():
    common = set()
    filepath = os.path.join(os.path.dirname(__file__), 'wordlists', 'common.txt')
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                common.add(line.strip().lower())
    except FileNotFoundError:
        print("⚠️  Warning: common.txt not found. Skipping common password check.")
    
    return common


def is_common_password(password, common_passwords):
    return password.lower() in common_passwords