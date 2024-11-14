"""

Objective:

Define a function called calculate_total that:

Accepts any number of positional arguments for item prices.
Accepts keyword arguments for optional additional charges (e.g., tax, discount, shipping).

Calculate the total price by:
Summing up all the item prices from *args.
Adding any additional charges from **kwargs.
Return the final total amount.

"""

def calculate_total(*item_prices, **additional_charges):
    sum_of_prices = sum(item_prices)
    sum_of_prices += sum(additional_charges.values())
    return sum_of_prices


calculation = calculate_total(10.99, 20.75, 3.50, tax=2.5, discount=-5.00)
print(f"Total Costs: ${calculation}")