
import random
import string


def generate_verification_code():
    digits = string.digits
    verification_code = ''.join(random.choice(digits) for i in range(6))
    return verification_code
