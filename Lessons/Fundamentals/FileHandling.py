import os

# File detection:
file_path = "text.txt"

if os.path.exists(file_path):
    print(f"It exists. Location File Path: {file_path}.")
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("This is a directory.")
else:
    print("It doesn't exist")



# File writing:
text_data = "Random Data Testing Testing"

with open(file_path, "w") as file:
    file.write(text_data)
    print(f"text file {file_path} was created.")


# pathlib
from pathlib import Path

print(os.getcwd())
Path("Directory1").mkdir(parents=True, exist_ok=True)
print(os.path.isdir("Directory1"))

try:
    with open("non_existent_file.txt", "r") as file2:
        content = file2.read()
        print(content)
except FileNotFoundError:
    print("That file doesn't exist.")


# exercise
Path("NewDirectory").mkdir(exist_ok=True)
file = Path("NewDirectory/text_example.txt")

with open(file, "w") as file3:
    file3.write("Hello hello.")

with open(file, "r") as file4:
    if Path(file).exists():
        content = file4.read()
        print(content)
    else:
        print("That file doesn't exist.")


# better version
from pathlib import Path

# Create a new directory
directory = Path("NewDirectory")
directory.mkdir(exist_ok=True)

# Create a file path
file = directory / "text_example.txt"

# Write to the file
file.write_text("Hello hello.")

# Read and check if the file exists
if file.exists():
    content = file.read_text()
    print(content)
else:
    print("That file doesn't exist.")
