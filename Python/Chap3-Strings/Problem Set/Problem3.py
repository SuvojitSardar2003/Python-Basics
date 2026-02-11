# 3. WAP to detect double spaces in a string.
name = "Suvojit is a good  boy and  "

print(name.find("  "))

# 4. Replace double space from Problem 3 with single spaces.

print(name.replace("  "," "))

print(name) # Strings are immutable which means that you cannot change them by running functions on them.

# 5. WAP to format the following letter using ecscape sequences characters.

letter = "Dear Harry,\n\tThis Python Course is nice.\nThanks!"

print(letter)