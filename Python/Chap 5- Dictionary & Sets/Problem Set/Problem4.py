# 4. What will be the length of following set S:

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# The length of the set S will be 2 because 20 (int) and 20.0 (float) are considered equal in Python, while "20" (str) is different. Therefore, the set will contain only two unique elements: {20, '20'}.