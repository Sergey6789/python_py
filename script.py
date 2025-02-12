import secrets
import string

def create_password(size):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(size))
print(create_password(12))