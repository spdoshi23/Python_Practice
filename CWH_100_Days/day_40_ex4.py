# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

msg = input("Enter the message you want to code or decode: ")
task = int(input("Enter 0 if you want to code or enter 1 if you want to decode: "))

ls0 = []
if task == 0:
    ls0 = msg.split()
    results0 = []
    for words in ls0:
        if len(words) < 3:
            modification0 = words[::-1]
            results0.append(modification0)
        elif len(words) >= 3:
            start_chars = ''.join(random.choices(string.ascii_lowercase, k=3))
            end_chars = ''.join(random.choices(string.ascii_lowercase, k=3))

            modification0 = start_chars + words[1:] + words[0] +end_chars
            results0.append(modification0)
    print(" ".join(results0))

ls1 = []
if task == 1:
    ls1 = msg.split()
    results1 = []
    for words in ls1:
        if len(words) < 3:
            modification1 = words[::-1]
            results1.append(modification1)
        elif len(words) >= 3:
            words = words[3:len(words)-3]
            modification1 = words[-1] + words[0:len(words)-1]
            results1.append(modification1)
    print(" ".join(results1))

