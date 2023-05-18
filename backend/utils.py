
# TODO: Implement password hashing with bcrypt
def password_hash(hashed_password: str) -> str:
    return password

def password_verify(password: str, hashed_password: str) -> bool:
    return password_hash(password) == hashed_password
