# lambda = small, anonymous function, typicall one-liners and used for short simple operations

# syntax: lambda arguments: expression


def add(x,y):
    return x+y


add_lambda = lambda x,y: x+y

print(add(3, 5))
print(add_lambda(3, 5))


# real world example of using lambdas with the map() function
# map() = applies a given function to each element of an iterable (list, tuple, etc.)

price_data = ["$10.99", "$23.45", "$50.00", "$9.99", "$14.75"]

# Lambda to clean and convert price to float
clean_price = lambda price_str : price_str.replace("$", "")

# Use map() to apply the clean_price lambda to each element in the price_data list
cleaned_prices = map(clean_price, price_data)

print(list(cleaned_prices))  # Output: [10.99, 23.45, 50.0, 9.99, 14.75]
