from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int = 8) -> str:
    str_ = ascii_uppercase + ascii_lowercase + digits
    return "".join(sample(str_, n))

print(get_random_password())
