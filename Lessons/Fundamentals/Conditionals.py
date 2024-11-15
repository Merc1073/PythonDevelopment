age = 20

# Below is an IF statement: they execute code based on conditions

# if this condition is true...
if age < 0:
    # ...then execute this code
    print("You have not been born yet!")

# if the above condition is not true, but this one is...
elif age < 18:
    # ...then execute this code instead
    print("You are a minor.")

elif age >= 18:
    print("You are an adult.")
# if none of the conditions above are true...
else:
    # ...then execute this code instead
    print("You are an adult.")


"""Comparison Operators:

'==' checks if two values are equal
'!=' checks if two values are NOT equal
'<, >, <=, >=' Less than, Greater than, Less than or Equal to, Greater than or Equal to

"""

"""Logical Operators:

'and': Both conditions must be true
'or':  At least one condition must be true
'not': Inverts the condition

"""

age2 = 37
has_permission = True

if age2 > 20 and has_permission:
    print("You can enter.")
else:
    print("You may not.")