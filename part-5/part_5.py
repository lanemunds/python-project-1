### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here



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
    with open("library.txt", "a") as f:
          f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
        


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


def see_books(book_source):

    print("\nHere are all your books...\n")

    with open(book_source, "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            
            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
        }

            print(
                f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")
            
            
           


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def home_page():
    quit = True
    while quit == True:
        in_select = int(input("to add a book type 1... to view all book type 2.... To quit type 3... to find total number of pages type 4... to find books by an author type 5... to find the average rating type 6... to find the average number of pages type 7...- "))
        if in_select == 1:
            add_book()
        elif in_select == 2:
            see_books("library.txt") 
        elif in_select == 3:
            quit = False       
        elif in_select == 4:
            total_pages()
        elif in_select == 5:
            author_list(input("type an authors name- "))
        elif in_select == 6:
            avg_rtng()
        elif in_select == 7:
            avg_pages()
            
           
        else:
            print('please select an option from the menu')    
        
        
        



    



### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def total_pages():
    total = 0
    with open("library.txt","r") as f:
        for line in f:
            mylist = line.split(',')
            total = total + int(mylist[4])
        print(total)    
            
   


def author_list(author_name):
    resp_list =[]
    with open('library.txt', 'r') as f:
        for line in f:
            mylist = line.split(',')
            if mylist[1] == author_name:
                resp_list.append(mylist[0])
        print(resp_list)
           


def avg_rtng():
    total = 0
    count = 0
    with open("library.txt","r") as f:
        for line in f:
            mylist = line.split(',')
            total = total + float(mylist[3])
            count = count + 1
        print(total/count)    
            
def avg_pages():
    total = 0
    count = 0
    with open("library.txt","r") as f:
        for line in f:
            mylist = line.split(',')
            total = total + float(mylist[4])
            count = count + 1
        print(total/count)    
            



if __name__=="__main__":
    home_page()   
