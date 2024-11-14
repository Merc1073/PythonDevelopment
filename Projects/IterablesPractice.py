"""

Objective:

Write a function called count_vowels that:

1. Takes a single string as input.
2. Iterates through each character in the string.
3. Counts how many vowels ('a', 'e', 'i', 'o', 'u') are present,
regardless of whether they are uppercase or lowercase.

The function should return the total count of vowels.

"""

def count_vowels(string_input):
    vowel_count = 0
    vowels = ['a', 'e', 'i' , 'o', 'u']
    string_input = string_input.lower()
    for vowel in string_input:
        if vowel in vowels:
            vowel_count+=1
    return vowel_count

total = count_vowels("This is an example of a sentence")
print(f"Total number of vowels in your sentence: {total}.")