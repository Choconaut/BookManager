import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    1: 'Search all books',
    2: 'Search by Title', #zero or more book returned
    3: 'Search by ISBN', #zero or one books returned
    4: 'Search by Publisher', #zero or more books returned
    5: 'Search by Price Range', #zero or more books returned
    6: 'Search by Year', #zero or more books returned
    7: 'Search by Title and Publisher' #zero or more books returned
}

edit_menu_options = {
    1: 'Edit ISBN',
    2: 'Edit Title',
    3: 'Edit Year',
    4: 'Edit Publisher',
    5: 'Edit Previous Edition',
    6: 'Edit Price'
}

def search_all_books():

    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item[0], item[1])
    print("---End of Search Results---")


def search_by_title(title):
    results = book_dao.findByTitle(title) #title from console
    print("Search by Title:")
    s_format = "%-10s %-1s %-50s" # format specifiers that indicate left-aligned fields of specific widths (10, 1, and 50 respectively)
    print(s_format % ("ISBN:", "|", "Title:"))
    # prints book entries with given title (0 or more results)
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(s_format % (item[0], "|", item[1]))
    print("---End of Search Results---")

def search_by_isbn(isbn):
    results = book_dao.findByISBN(isbn) #isbn from console
    print("Search by ISBN:")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(item[0], "|", item[1])

def search_by_publisher(publisher):
    results = book_dao.findByPublisher(publisher) #publisher from console
    print("Search by Publisher:")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(item[0], "|", item[1])

def search_by_price_range(min_price, max_price):
    results = book_dao.findByPriceRange(min_price, max_price) #min_price and max_price from console
    print("Search by Price Range:")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(item[0], "|", item[1])

def search_by_year(year):
    results = book_dao.findByYear(year) #year from console
    print("Search by Year:")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(item[0], "|", item[1])

def search_by_title_and_publisher(title, publisher):
    results = book_dao.findByTitleAndPublisher(title, publisher) #title and publisher from console
    print("Search by Title and Publisher:")
    if len(results) == 0:
        print("N/A")
    else:
        for item in results:
            print(item[0], "|", item[1])

def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()
    print("---End of Menu---")
    print()

def print_search_menu():
    print()
    print("Please make a selection")
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()
    print("---End of Search Menu---")
    print()

def print_edit_menu():
    print()
    print("Please make a selection")
    for key in edit_menu_options.keys():
        print (str(key)+'.', edit_menu_options[key], end = "  ")
    print()

def option1():  # add a publisher
    print()
    print("-------Add Publisher-------")
    print("Type NULL for no entry.")
    name = input("Enter Name: ")
    phone = ""
    while phone == "":
        phone = input("Enter Phone Number: ")
        if len(phone) != 10:
            phone = ""
            print("Error: Phone number length must be 10!")
        try:
            int(phone)
        except ValueError:
            phone = ""
            print("Error: Phone number must consist of integers!")
    city = ""
    while city == "":
        city = input("Enter City: ")
        if len(city) > 20:
            city = ""
            print("Error: City name too long (max 20 characters)!")
    result = book_dao.addPublisher(name, phone, city)
    if result == False:
        print("Error: Publisher already exists!")
    else:
        print("Publisher added successfully!")


def option2(): # add a book
    print('Handle option \'Option 2\'')
    print('Add a book')
    print('Type NULL for no entry.')
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    while title == "":
        title = input("Enter Title: ")
        if len(title) > 50:
            title = ""
            print("Error: Title too long (max 50 characters)!")
    year = ""
    while year == "":
        year = input("Enter Year: ")
        if len(year) != 4:
            year = ""
            print("Error: Year must be 4 digits!")
        try:
            int(year)
        except ValueError:
            year = ""
            print("Error: Year must consist of integers!")
    published_by = input("Enter Publisher: ")
    while published_by == "":
        published_by = input("Enter Publisher: ")
        if len(published_by) > 25:
            published_by = ""
            print("Error: Publisher name too long (max 25 characters)!")
    previous_edition = input("Enter Previous Edition: ")
    while previous_edition == "":
        previous_edition = input("Enter Previous Edition: ")
        if previous_edition != "NULL":
            previous_edition = ""
            print("Error: Previous Edition must be NULL or 10 digits!")
        elif len(previous_edition) > 10:
            previous_edition = ""
            print("Error: Previous Edition must be at most 10 digits!")
        try:
            int(previous_edition)
        except ValueError:
            previous_edition = ""
            print("Error: Previous Edition must consist of integers!")
    price = ""
    while price == "":
        price = input("Enter Price: ")
        try:
            float(price)
        except ValueError:
            price = ""
            print("Error: Price must consist of integers!")
    result = book_dao.addBook(isbn, title, year, published_by, previous_edition, price)
    if result == 0:
        print("Error: Book does not exist!")
    elif result == 1:
        print("Error: Publisher does not exist!")
    elif result == 2:
        print("Error: Previous edition does not exist!")
    elif result == 3:
        print("Book added successfully!")

def option3(): #edit a book
    print('Handle option \'Option 3\'')
    print('Edit a book')
    print()
    isbn = input("Enter ISBN of the book to edit: ")
    print_edit_menu()
    print("Enter the numbers of the fields to edit (e.g., '2 3 6'): ")
    print("Leave out numbers of fields you do not wish to edit.")
    selected_fields = input("Enter Values:")
    numbers = selected_fields.split()
    selected_numbers = [int(num) for num in numbers]

    new_isbn = ""
    title = ""
    year = ""
    published_by = ""
    previous_edition = ""
    price = ""

    #Want to change to this to something similar to a switch statement, but unsure of implementation
    for i in range(len(selected_numbers)):
        if selected_numbers[i] == 1:
            new_isbn = input("Enter ISBN: ")
            while new_isbn == "":
                new_isbn = input("Enter ISBN: ")
                if len(new_isbn) > 10:
                    new_isbn = ""
                    print("Error: ISBN must be at most 10 digits!")
            try:
                int(new_isbn)
            except ValueError:
                isbn = ""
                print("Error: ISBN must consist of integers!")
                return
        elif selected_numbers[i] == 2:
            title = input("Enter Title: ")
            while title == "":
                title = input("Enter Title: ")
                if len(title) > 50:
                    title = ""
                    print("Error: Title too long (max 50 characters)!")
        elif selected_numbers[i] == 3:
            year = ""
            while year == "":
                year = input("Enter Year: ")
                if len(year) != 4:
                    year = ""
                    print("Error: Year must be 4 digits!")
                try:
                    int(year)
                except ValueError:
                    year = ""
                    print("Error: Year must consist of integers!")
        elif selected_numbers[i] == 4:
            published_by = input("Enter Publisher: ")
            while published_by == "":
                published_by = input("Enter Publisher: ")
                if len(published_by) > 25:
                    published_by = ""
                    print("Error: Publisher name too long (max 25 characters)!")
        elif selected_numbers[i] == 5:
            previous_edition = input("Enter Previous Edition: ")
            while previous_edition == "":
                previous_edition = input("Enter Previous Edition: ")
                if previous_edition != "NULL":
                    previous_edition = ""
                    print("Error: Previous Edition must be NULL or 10 digits!")
                elif len(previous_edition) > 10:
                    previous_edition = ""
                    print("Error: Previous Edition must be at most 10 digits!")
                try:
                    int(previous_edition)
                except ValueError:
                    previous_edition = ""
                    print("Error: Previous Edition must consist of integers!")
        elif selected_numbers[i] == 6:
            price = ""
            while price == "":
                price = input("Enter Price: ")
                try:
                    float(price)
                except ValueError:
                    price = ""
                    print("Error: Price must consist of integers!")
    result = book_dao.editBook(selected_numbers, isbn,new_isbn, title, year, published_by, previous_edition, price)
    if result == 0:
        print("Error: Book does not exist!")
    elif result == 1:
        print("Error: New ISBN already exists!")
    elif result == 2:
        print("Error: Publisher does not exist!")
    elif result == 3:
        print("Error: Previous edition does not exist!")
    elif result == 4:
        print("Book edited successfully!")


def option4(): #delete a book
    print('Handle option \'Option 4\'')
    print('Delete a book')
    isbn = input("Enter ISBN: ")
    try:
        int(isbn)
    except ValueError:
        isbn = ""
        print("Error: ISBN must consist of integers!")
        return
    result = book_dao.deleteBook(isbn)
    if result == 0:
        print("Error: Book not found!")
    else:
        print("Book deleted successfully!")
def option5():
    # A sub-menu shall be printed
    # and prompt user selection
    # print_search_menu
    print_search_menu()

    # user selection of options and actions
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except:
        print('Wrong input. Please enter a number')

    # Check what choice was entered and act accordingly
    if option == 1: # Assume the option: search all books was chosen
        print("Search Option 1: Return All Books.")
        search_all_books()
    elif option == 2: # Assume the option: search by title was chosen
        print("Search Option 2: Search By Title.")
        title = input("Enter Title: ")
        search_by_title(title)
    elif option == 3: # Assume the option: search by ISBN was chosen
        print("Search Option 3: Search By ISBN.")
        isbn = input("Enter ISBN: ")
        search_by_isbn(isbn)
    elif option == 4: # Assume the option: search by publisher was chosen
        print("Search Option 4: Search By Publisher.")
        publisher = input("Enter Publisher: ")
        search_by_publisher(publisher)
    elif option == 5: # Assume the option: search by price range was chosen
        print("Search Option 5: Search By Price Range.")
        min_price = input("Enter Minimum Price: ")
        max_price = input("Enter Maximum Price: ")
        search_by_price_range(min_price, max_price)
    elif option == 6: # Assume the option: search by year was chosen
        print("Search Option 6: Search By Year.")
        year = input("Enter Year: ")
        search_by_year(year)
    elif option == 7:  # Assume the option: search by title and publisher was chosen
        print("Search Option 7: Search By Title and Publisher.")
        title = input("Enter Title: ")
        publisher = input("Enter Publisher: ")
        search_by_title_and_publisher(title, publisher)
    else:
        print('Invalid option. Please enter a number between 1 and 7.')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number')

        # Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')











