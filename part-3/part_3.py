my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parse(book):
    book_string = f"{book['title']} was written by {book['author']} in {book['year']}. it has a rating of {book['rating']} and {book['pages']} pages."
    print(book_string)
    
book_parse(my_book)


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def find_author(book):
    author_string= f"the author of the book is {book['author']}"
    print(author_string)
def find_title(book):
    title_string= f"the title of the book is {book['title']}"
    print(title_string)
def find_year(book):
    year_string= f"the book was written in {book['year']}"
    print(year_string)
def find_rating(book):
    rating_string= f"the rating of the book is {book['rating']}"
    print(rating_string)
def find_pages(book):
    pages_string= f"the book has {book['pages']} pages"
    print(pages_string)
    
find_author(my_book)    
find_title(my_book)    
find_year(my_book)    
find_rating(my_book)    
find_pages(my_book)    

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def shorter_book(book1,book2):
    if book1['pages'] < book2['pages']:
        return f"{book1['title']} has fewer pages"
    elif book2['pages']<book1['pages']:
        return f"{book2['title']} has fewer pages"
    else:
        return "these books have the same amount of pages"
    
    
def better_book(book1,book2):
    if book1['rating'] > book2['rating']:
        return f"{book1['title']} has a higher rating"
    elif book2['rating']>book1['rating']:
        return f"{book2['title']} has a higher rating"
    else:
        return "these books have the same rating"
    
def older_book(book1,book2):
    if book1['year'] < book2['year']:
        return f"{book1['title']} is the older book"
    elif book2['year']<book1['year']:
        return f"{book2['title']} is the older book"
    else:
        return "these books were written in the same year."
    
        