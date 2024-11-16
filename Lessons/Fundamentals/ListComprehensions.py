# list comprehensions

squares = [x**2 for x in range(1, 6)]
print(squares)

example_list = [x for x in range(1, 10)]

print(example_list)

odd_squares = [x**2 for x in range(1, 21) if x % 2 == 1]
print(odd_squares)

test_list = [x*x for x in range(1, 30) if x % 3 == 0]
print(test_list)