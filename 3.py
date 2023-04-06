# Chistian Dating | BSCPE 1-5

input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" * 80)

# Intro
import pyfiglet
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

# To remove spaces or whitespaces.
def remove_space(a):
    a = a.upper()
    for i in a:
        if " " in i:
            a = a.replace(i, "")
    print("\n\033[96mTranslated:", a)
    return a

def to_number(a, b):
    for i in a:
        if i in letter_to_number:
            b.append(letter_to_number[i])
 
def list_to_strings(a, b):
    for i in a:
        b = b + (str(i) + " ")
    return b

# Conversion
letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
letter_to_number_rev = {number: letter for letter, number in letter_to_number.items()}

print("\033[90m=" * 80)

# Problem 3 - The Vigenère Cipher

# For inputted message. 
message = input("\n\033[92mYour Message: ")
message = remove_space(message)

# For inputted key.
key = input("\n\033[92mYour Key: ")
key = remove_space(key)

message_number, key_number, sum_number, mod_number = [], [], [], []
cipher, message_cipher, key_cipher, keys, messages, add, mod = "", "", "", "", "", "", ""

if len(key) < len(message):
    number_rep = len(message) // (len(key)) + 1
    messages = message
    keys = (key * number_rep)[:len(message)]
elif len(key) > len(message):
    number_rep = len(key) // (len(message)) + 1
    keys = key
    messages = (message * number_rep)[:len(key)]
else:
    keys = key
    messages = message

print("\033[90m=" *80)

to_number(messages, message_number)
to_number(keys, key_number)

print("\n\033[96mMESSAGE:", message, list_to_strings(message_number, message_cipher))
print("\n\033[96mKEY:", key, list_to_strings(key_number, key_cipher),)

for a in range(len(message)):
    sum_number.append((message_number[a] + key_number[a]))

print("\n\033[96mADD: ", list_to_strings(sum_number, mod))

for b in range(len(message)):
    mod_number.append((message_number[b] + key_number[b]) % 26)

print("\n\033[96mMOD: ", list_to_strings(mod_number, mod))

for c in mod_number:
    if c in letter_to_number_rev:
        cipher += (str(letter_to_number_rev[c]) + " ")

print("\n\033[96mCIPHERTEXT:", cipher)

# Outro
print("\033[90m=" *80)
greet1 = "THANK YOU!"
print("\033[92m" + pyfiglet.figlet_format(greet1, font = "bubble"))

print("\033[90m=" *80)