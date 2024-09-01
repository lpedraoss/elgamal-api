import random
from math import pow

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def gen_key(p):
    key = random.randint(int(pow(10, 20)), p)
    while gcd(p, key) != 1:
        key = random.randint(int(pow(10, 20)), p)
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

def encrypt(msg, p, e, g):
    en_msg = []
    k = gen_key(p)
    c1 = power(g, k, p)
    s = power(e, k, p)
    for i in range(0, len(msg)):
        en_msg.append(s * ord(msg[i]))
    return en_msg, c1

def decrypt(en_msg, p, a, c1):
    dr_msg = []
    h = power(c1, a, p)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))
    return dr_msg

def verify_password(input_password, stored_encrypted_password, p, a, c1):
    decrypted_stored_password = decrypt(stored_encrypted_password, p, a, c1)
    decrypted_stored_password_str = ''.join(decrypted_stored_password)
    return input_password == decrypted_stored_password_str