"""

import math
from datetime import datetime, timedelta
import random
import os
import sys
import json
import re
from collections import Counter, deque, defaultdict
import itertools
import time




print(math.sqrt(16))     # Square root: 4.0
print(math.factorial(5)) # Factorial: 120
print(math.pi)           # Pi: 3.141592653589793
print(math.sin(math.pi / 2)) # Sine of 90 degrees: 1.0




now = datetime.now()
print(now)  # Current date and time

one_week_later = now + timedelta(weeks=1)
print(one_week_later)  # Date and time one week from now

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Formatted date string





print(random.randint(1, 10))           # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Randomly selects an item
print(random.sample(range(10), 5))     # Randomly selects 5 items from a range




print(os.getcwd())  # Current working directory
os.mkdir('new_folder')  # Creates a new folder
print(os.listdir())  # Lists files and directories in the current folder
os.remove('file.txt')  # Deletes a file (if it exists)




print(sys.version)       # Python version
print(sys.argv)          # List of command-line arguments
#sys.exit()               # Exits the program




# Convert a Python dictionary to JSON string
data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Alice", "age": 25}'

# Convert JSON string back to Python dictionary
data = json.loads(json_string)
print(data['name'])  # Alice





text = "The rain in Spain"
pattern = r"\bS\w+"

matches = re.findall(pattern, text)
print(matches)  # ['Spain']





# Counter: Counts occurrences of items
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counts)  # Counter({'a': 3, 'b': 2, 'c': 1})

# deque: Double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # deque([0, 1, 2, 3, 4])

# defaultdict: Dictionary with a default value for missing keys
dd = defaultdict(int)
dd['a'] += 1
print(dd['a'])  # 1
print(dd['b'])  # 0 (default int is 0)





# Chain: Combine multiple iterables
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)  # 1, 2, 'a', 'b'

# Combinations: Get combinations of items
for combo in itertools.combinations([1, 2, 3], 2):
    print(combo)  # (1, 2), (1, 3), (2, 3)




print(time.time())  # Current time in seconds since the Epoch
time.sleep(2)       # Pauses execution for 2 seconds

# Measuring execution time
start = time.time()
# some code
end = time.time()
print("Execution time:", end - start, "seconds")


"""