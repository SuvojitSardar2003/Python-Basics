# 7. Write a python function to remove a given word from a list ad strip it at the same time.

# strip is used to remove leading and trailing whitespace from a string. In this case, we will use it to remove the given word from the list.

def remove(list, word):
    n = []
    if(word in list):
        list.remove(word)
    if not (word in list):
        for i in list:
            n.append(i.strip(word))
    return n

list = ["aapple", "banana", "cherrya", "datea", "elderberrya"]
print(remove(list, "banana"))