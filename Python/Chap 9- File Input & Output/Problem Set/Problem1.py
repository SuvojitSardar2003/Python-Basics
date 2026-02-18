# 1. WAP to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

f = open("poem.txt")

data = f.read()

if("twinkle" in data):
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()