import random
import json

vuse = input("What's this password for? - ")

vabc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
v123 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
vsign = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "="]
vbc = [vabc, v123, vsign]
vnum = 0
vbpass = []

while vnum < 8:
        vv = random.choice(vbc)
        vc = random.choice(vv)
        vbpass.append(vc)
        vnum += 1

vapass = ''.join(map(str, vbpass))

pwfData = {}
pwfData[vuse] = vapass

if vuse == "":
        print("Your password is -", vapass)
else:
        with open("Passwords.json", "a") as pwfa:
                pwfa.write(json.dumps(pwfData))
        print("Your password for", vuse, "is -", vapass)