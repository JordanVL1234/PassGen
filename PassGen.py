import random
import json

## What's the password for? ##
vuse = input("What's this password for? - ")

## PassGen ##
vabc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
v123 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
vsign = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "="]
vv = [vabc, v123, vsign]

## PassGen ##
v1 = random.choice(vv)
c1 = random.choice(v1)
v2 = random.choice(vv)
c2 = random.choice(v2)
v3 = random.choice(vv)
c3 = random.choice(v3)
v4 = random.choice(vv)
c4 = random.choice(v4)
v5 = random.choice(vv)
c5 = random.choice(v5)
v6 = random.choice(vv)
c6 = random.choice(v6)
v7 = random.choice(vv)
c7 = random.choice(v7)
v8 = random.choice(vv)
c8 = random.choice(v8)

## The Output ##
vpass = [c1, c2, c3, c4, c5, c6, c7, c8]
with open("Password.json", "w") as f:
        json.dumps([vuse, " - ", vpass])
print("Your password for ", vuse, " is - ", *vpass, sep='')