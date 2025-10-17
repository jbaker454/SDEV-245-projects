import hashlib

# vurnability Cryptographic Failures
# issue sha1 decryption broken


def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

# fixed version
# uses sha256, should include something so the user can't try billions per second but eh

def hash_password_fixed(password):
    return hashlib.sha256(password.encode()).hexdigest()