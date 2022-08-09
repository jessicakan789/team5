import hashlib


def hash_password(password):
    encoded_password = password.encode()
    stored_password = hashlib.md5(encoded_password).hexdigest()

    return stored_password
