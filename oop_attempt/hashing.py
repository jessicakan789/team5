import hashlib

def hash_password(password):
    encode_pwrd = password.encode()
    pwrd_hash = hashlib.md5(encode_pwrd).hexdigest()
    return pwrd_hash

