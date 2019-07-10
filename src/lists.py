# Step 2
fruit_list = ['apple', 'orange', 'peach', 'pear', 'plum']
print(fruit_list)
print(fruit_list[1])

# Step 3
fruit_list.append('strawberry')
print(fruit_list)

# Step 4
veg_list = ['tomato', 'cucumber']
fruit_veg_list = fruit_list + veg_list
print(fruit_veg_list)

# Start Dictionaries section
books = {
    'The Hunger Games': 'Susan Collins',
    'Harry Potter': 'J K Rowling',
    'Lord of the Rings': 'Tolkien'
}

# Step 2 modified (using f-strings rather than % replace)
for book, author in books.items():
    print(f"Author of {book} is {author}")

# Time to work with Sets

# Step 1
a = set("my name is Susan and Susan is my name".split())
print(a)
b = set("my month is june and june is my month".split())
print(b)


# Step 2
print(a.intersection(b))

# Step 3
print(a.symmetric_difference(b))

# Step 4
print(a.union(b))


# Starting the conditional part of the training

# Step 2: We want to see if the author of 'Harry Potter'
# is JK Rowling. If so, print a message.
author_of_harry_potter = books['Harry Potter']
if author_of_harry_potter == 'J K Rowling':
    print(f"{author_of_harry_potter} is the author of Harry Potter!")

# Step 3
fruit = "raspberry"
if fruit in fruit_list:
    print(f"{fruit} is a fruit")

# Step 4
if fruit in fruit_list:
    print(f"{fruit} is a fruit")
elif fruit in ["blueberry", "blackberry", "raspberry"]:
    print(f"{fruit} is a berry")
else:
    print(f"{fruit} is not a fruit")

# Practice Exercise 1 and 2
target_fruit = 'pear'
for fruit in fruit_list:
    print(fruit)
    if fruit == target_fruit:
        print(f"Fruit is a {target_fruit}. We're breaking out of here!")
        break


