import random
import string

def random_number(low = 0,high = 100):
    return random.randint(low,high)

def random_list(n = 5,low = 0,high = 100):
    return [random.randint(low,high)for _ in range(n)]

def random_password(length=8):
    if length<=4:
        length = 4
    chars = string.ascii_letters + string.digits + string.punctuation
    password=[
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
        ]
    password += [random.choice(chars) for _ in range(length-4)]
    random.shuffle(password)
    return''.join(password)

def generate_otp(digits=6):
    if digits <=0:
        raise ValueError("digits must be positive")
    start = 10**(digits-1)
    end = (10**digits)-1
    return str(random.randint(start,end))

