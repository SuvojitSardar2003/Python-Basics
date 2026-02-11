print("Suvojit Sardar")
print("Suvojit\nSardar")
print("Suvojit\"Sardar")
print("Suvojit\Sardar")

name="Suvo"
print(name+" is cool")

print("lower()="+name.lower())
print("upper()="+name.upper())
print("islower()=")
print(name.islower())
print("isupper()=")
print(name.isupper())
print(name.upper().isupper())
print(name.lower().islower())

print("len()=")
print(len(name))
print("Individual char="+name[1])
print("Individual char(upper)="+name[3].upper())

print("index() of \"S\"=")
print(name.index("S"))

print("replace() of \"Suvo\" to \"Suvojit\"=")
print(name.replace("Suvo","Suvojit"))