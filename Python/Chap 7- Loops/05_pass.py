#pass
# The pass statement is a null operation that does nothing when executed. It is often used as a placeholder where syntactically a statement is required but no action is desired.
for i in range(10):
    if i == 5:
        pass  # Do nothing when i equals 5
    else:
        print(i)

# is continue and pass same?
# No, continue and pass are not the same. The continue statement is used to skip the current iteration of a loop and move on to the next iteration, while the pass statement does nothing and is simply a placeholder. In the example above, when i equals 5, the pass statement is executed, which means that nothing happens and the loop continues to the next iteration without printing anything for i equals 5.

for i in range(645):
    pass

i = 0
while(i<45):
    print(i)
    i += 1