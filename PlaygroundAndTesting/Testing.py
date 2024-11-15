def check_palindrome(input_string):
    if input_string == input_string[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

def iterate_over_dict(dictionary):
    for key, value in dictionary.items():
        print(key, ":", value)

dict_example = {
    "GPA1" : 4.0,
    "GPA2" : 3.5,
    "GPA3" : 2.7
}

#print(dict_example["GPA4"])

#iterate_over_dict(dict_example)



class BankAccount:

    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: £{self.balance:.2f}")

    def withdraw(self, amount):
        temp = self.balance - amount
        if self.balance <= 0 or temp <= 0:
            print("Can't withdraw, not enough money.")
        else:
            self.balance -= amount
            print(f"New balance: £{self.balance:.2f}")

    def display_balance(self):
        print(f"Your current balance: £{self.balance:.2f}")


bank1 = BankAccount()
bank1.display_balance()
bank1.deposit(100)
bank1.display_balance()
bank1.withdraw(50)
bank1.withdraw(6000)


with open("text.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.show()

from pathlib import Path

#Path("NewDirectory/Directory").exists()


import asyncio

async def task1():
    print("Doing task...")
    await asyncio.sleep(2)
    print("Task done.")

asyncio.run(task1())