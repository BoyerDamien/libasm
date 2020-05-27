import random
import string

def random_string(length):
    string_len = random.randint(1, length)
    string_params = [random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(string_len)]
    return "".join(string_params)