# generator expression = creates an array that, when printing out a value/element, instantly deletes
#                        it from the array, saving memory

gen = (x**2 for x in range(1, 6))
print(gen)  # Output: <generator object <genexpr> at 0x...>

for value in gen:
    print(value)


gen2 = (x**2 for x in range(1, 20) if x % 4 == 0)

print(sum(gen2))