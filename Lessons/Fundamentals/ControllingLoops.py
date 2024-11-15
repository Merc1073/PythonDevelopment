# break = exits the loop when encountered
# continue = skips over current iteration

# should print 1 to 10, but once i reaches 5, it exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)

print()
print()

# skips over the iteration where i = 3, then continues the rest of the loop
for i in range(10):
    if i == 3:
        continue
    print(i)