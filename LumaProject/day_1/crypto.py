import secrets
import string

# def generate_random_password(length=16):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(secrets.choice(characters) for _ in range(length))
#     return password
#
# password = generate_random_password()
# print(password)


def generate_hash(password: str):
    import hashlib
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

print(f'Generating hash: {generate_hash("password")}')