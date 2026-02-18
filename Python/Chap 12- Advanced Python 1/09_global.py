a = 89

def fun():
    #global a #it will change the global a
    a = 3
    print(a)

fun()
print(a)