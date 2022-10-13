### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
##def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = input("What year was this book published? - ")
#     rating = input("What rating out of 5 would you give this book? - ")
#     pages = input("What is the page count of the book? - ")
    
#     book_dictionary = {
#         "title":title,
#         "author":author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
    
#     return book_dictionary

# print(create_new_book())
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = int(input("What year was this book published? - "))
#     rating = float(input("What rating out of 5 would you give this book? - "))
#     pages = int(input("What is the page count of the book? - "))
    
#     book_dictionary = {
#         "title":title,
#         "author":author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     print(type(year))
#     print(type(rating))
#     print(type(pages))
    
#     return book_dictionary

# print(create_new_book())



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     try:
#         year = int(input("What year was this book published? - "))
#     except:    
#         year = int(input("Please type a number for the year - "))
#     try:
#         rating = float(input("What rating out of 5 would you give this book? - "))
#     except:    
#         rating = float(input("Please type a number for the rating - "))
#     try:
#         pages = int(input("What is the page count of the book? - "))
#     except:    
#         pages = int(input("Please type a number for the number of pages - "))
    
#     book_dictionary = {
#         "title":title,
#         "author":author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     print(type(year))
#     print(type(rating))
#     print(type(pages))
    
#     return book_dictionary

# print(create_new_book())




### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here



from turtle import home


my_books = [
    {
        "title": "Harry Potter",
        "author": "JK Rowling",
        "year": 1997,
        "rating": 4.8,
        "pages": 345
    },
    {
        "title": "Chamber of Secrets",
        "author": "JK Rowling",
        "year": 1999,
        "rating": 4.5,
        "pages": 400
    },
    {
        "title": "Prisoner of Azkiban",
        "author": "JK Rowling",
        "year": 2002,
        "rating": 4.9,
        "pages": 313
    },
    {
        "title": "half blood prince",
        "author": "JK Rowling",
        "year": 209,
        "rating": 4.2,
        "pages": 502
    }
]

def add_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:    
        year = int(input("Please type a number for the year - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:    
        rating = float(input("Please type a number for the rating - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:    
        pages = int(input("Please type a number for the number of pages - "))
    
    book_dictionary = {
        "title":title,
        "author":author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    my_books.append(book_dictionary)
    print(book_dictionary)
    

def see_books():
    for books in my_books:
        print(books)
      



# def home_page():
#         in_select = int(input("to add a book type 1. to view all book type 2. To quit type 3- "))
#         if in_select == 1:
#             add_book()
#         elif in_select == 2:
#             see_books() 
#         elif in_select == 3:
#             quit = False       
#         else:
#             print('please select an option from the menu')    
        
        
        
# home_page()        

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def home_page():
    quit = True
    while quit == True:
        in_select = int(input("to add a book type 1. to view all book type 2. To quit type 3- "))
        if in_select == 1:
            add_book()
        elif in_select == 2:
            see_books() 
        elif in_select == 3:
            quit = False       
        else:
            print('please select an option from the menu')    
        
        
        
home_page()        
