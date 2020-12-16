from passlib.hash import pbkdf2_sha256


def hash_password(password):
    return pbkdf2_sha256(password)


def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)

