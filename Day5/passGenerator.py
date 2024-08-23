import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# buffer creation
buffer = []

# letters amount
for count in range(nr_letters):
    rRange = random.randint(1, len(letters))
    buffer.append(letters[rRange - 1])

# numbers amount
for count in range(nr_numbers):
    rRange = random.randint(1, len(numbers))
    buffer.append(numbers[rRange - 1])

# symbols amount
for count in range(nr_symbols):
    rRange = random.randint(1, len(symbols))
    buffer.append(symbols[rRange - 1])

# shuffling + string print
random.shuffle(buffer)
buffToString = ''.join(buffer)
print(f"Here is your password: {buffToString}")

