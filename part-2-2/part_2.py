### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['JK Rowling', "Brandon Sanderson", "Adam Cox", "Adam Smith", "Dr Suess", "RL Stein", "JRR Tolkien", "George RR Martin"]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append("Lane Edmunds")

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove("RL Stein")
my_authors.pop()
print(my_authors)
print(my_authors[1:3])
# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
my_authors[1]

# Now slice the list.

# Code here
# Example: my_authors[1:4]
my_authors[2:2]

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

myTuple = ('JK Rowling', "Brandon Sanderson", "Adam Cox", "Adam Smith", "Dr Suess", "RL Stein", "JRR Tolkien", "George RR Martin")
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
authorSet = {'JK Rowling', "Brandon Sanderson", "Adam Cox", "Adam Smith", "Dr Suess", "RL Stein", "JRR Tolkien", "George RR Martin"}

# Add a new author to your set.

# Example: my_author_set.add("J.R.R. Tolkien")
authorSet.add("lane Edmunds")

# Try adding the same author again, and be sure to print your set.

authorSet.add('lane Edmunds')
print(authorSet)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

for h in authorSet:
    print(h)
    
for b in my_authors:
    print(b)
    
for a in myTuple:
    print(a)
    