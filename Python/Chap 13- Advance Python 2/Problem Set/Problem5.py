# 5. WAP to find maximum of the numbers in a list using the reduce function.

from functools import reduce
l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]

def greater(a,b):
    if(a>b):
        return a
    return b

max = reduce(greater, l)
print(max)

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# 7. Explore the 'Flask module and create a web server using Flask & Python