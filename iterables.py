#lists
fruits = ['apple', 'banana', 'cherry'] 
for fruit in fruits:
    print(fruit)
#strings
word = "hello"
for char in word:
    print(char)
#tuples
coordinates = (1, 2, 3)
for coord in coordinates:
    print(coord)
#dictionary
person = {'name': 'Alice', 'age': 25}
for key in person:
    print(key)  # iterates over keys

for value in person.values():
    print(value)  # iterates over values

for key, value in person.items():
    print(key, value)  # iterates over key-value pairs
#sets
unique_numbers = {1, 2, 3, 4}
for num in unique_numbers:
    print(num)
