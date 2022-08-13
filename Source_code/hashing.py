import hashlib


def hash_password(password):
    """
    This function performs hashing techniques on the input string, to return a hashed string.
    It utilises Pythons in-built hashlib module.

    :param password: (type: str)
    The string that needs hashing. This will be a password.

    :return:
    stored_password: (type: str)
    The hashed string.

    """
    encoded_password = password.encode()
    stored_password = hashlib.md5(encoded_password).hexdigest()

    return stored_password

