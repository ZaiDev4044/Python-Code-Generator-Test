import random
import time
import string

alpha="qwertyuioppasdfghjklmzxcvbn0123456789".upper()



while True :
    time.sleep(0.2)
    r1 = random.choice(alpha)
    r2 = random.choice(alpha)
    r3 = random.choice(alpha)
    r4 = random.choice(alpha)
    r5 = random.choice(alpha)
    r6 = random.choice(alpha)
    r7 = random.choice(alpha)
    r8 = random.choice(alpha)
    r9 = random.choice(alpha)
    r10 = random.choice(alpha)
    r11 = random.choice(alpha)
    r12 = random.choice(alpha)

    print(r1+r2+r3+r4+r5+r6+r9+r8+r9+r1+r11+r12)
