# Task 1: Sum of integers in a list
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
print("Sum of integers:", sum(numbers))

# Task 2: Favorite books in a tuple
books = ("1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "Moby Dick")
print("Favorite Books:")
for book in books:
    print(book)

# Task 3: Dictionary for storing person information
person = {}
person['name'] = input("Enter your name: ")
person['age'] = int(input("Enter your age: "))
person['favorite_color'] = input("Enter your favorite color: ")
print("Person Information:", person)

# Task 4: Common elements in two sets
set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

# Task 5: List comprehension for words with odd number of characters
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)

# Task 6: List operations
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
