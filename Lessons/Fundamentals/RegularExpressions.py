# regular expression (re, regex) = allows you to search, match and manipulate strings

import re


pattern = r"Hello"
text = "Hello World"

match = re.match(pattern, text)
if match:
    print("Match found: ", match.group())

print(match)


text = "Contact us at support@example.com or sales@example.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print("Emails found:", emails)