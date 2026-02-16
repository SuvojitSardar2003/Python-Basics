# 5. Repeat program 4 for list of such words to be censored.

words = ["Donkey","bad","ganda"]

with open("donkey.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkey.txt","w") as f:
    f.write(content)