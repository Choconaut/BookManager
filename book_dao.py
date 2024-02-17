from mysql_connector import connection

def findAll():
# returns all tuples in Book
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def findByTitle(title):
# returns all tuples in Book with specified title attribute
    cursor = connection.cursor()
    query = "SELECT Book.ISBN, Book.title FROM bookmanager.Book WHERE Book.title LIKE '%" + title + "%'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def findByISBN(isbn):
# returns all tuples in Book with specified ISBN attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.ISBN='" + isbn + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def findByPublisher(publisher):
# returns all tuples in Book with specified publisher attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.published_by='" + publisher + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def findByPriceRange(min_price, max_price):
# returns all tuples in Book with specified price attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.price between " + min_price + " and " + max_price
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def findByYear(year):
# returns all tuples in Book with specified year attribute
    cursor = connection.cursor()
    query = "select Book.ISBN, Book.title from bookmanager.Book where Book.year='" + year + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def findByTitleAndPublisher(title, publisher):
# returns all tuples in Book with specified title and publisher attributes
    cursor = connection.cursor()
    query = "SELECT Book.ISBN, Book.title FROM bookmanager.Book WHERE Book.title LIKE '%" + title + "%'" + " and Book.published_by='" + publisher + "'"

    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def addPublisher(name, phone, city):
# adds a new publisher to the Publisher table
    cursor = connection.cursor()
    if(checkPublisher(name) == True):
        return False
    query = "insert into bookmanager.Publisher values ('" + name + "', '" + phone + "', '" + city + "')"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return True #Publisher added successfully
def addBook(isbn, title, year, published_by, previous_edition, price):
# adds a new book to the Book table
    cursor = connection.cursor()
    if(checkIsbn(isbn) == True): #Check if the book already exists
        return 0 #Book already exists
    if(checkPublisher(published_by) == False): #Check if the publisher exists
        return 1 #Publisher does not exist
    if str.upper(previous_edition) != "NULL":  #Check if the previous edition exists
        query = "SELECT ISBN FROM bookmanager.Book WHERE ISBN = '" + previous_edition + "'"
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            return 2 #Previous edition does not exist
        query = "insert into bookmanager.Book values ('" + isbn + "', '" + title + "', '" + year + "', '" + published_by + "', '" + previous_edition + "', '" + price + "')"
    else:
        query = "insert into bookmanager.Book values ('" + isbn + "', '" + title + "', '" + year + "', '" + published_by + "', " + "NULL" + ", '" + price + "')"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    return 3 #Book added successfully

def deleteBook(isbn):
# deletes a book from the Book table
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where Book.ISBN='" + isbn + "'"
    cursor.execute(query)
    affected_rows = cursor.rowcount #Get the number of affected rows
    connection.commit()
    cursor.close()
    if affected_rows == 0:
        return False #Book does not exist
    else:
        return True


def editBook(selected_numbers, isbn, new_isbn, title, year, published_by, previous_edition, price):
# edits a book in the Book table
    cursor = connection.cursor()
    query = "Select * from bookmanager.Book where Book.ISBN='" + isbn + "'" #Check if the book already exists
    cursor.execute(query)
    results = cursor.fetchall()
    if not results:
        return 0 #Book does not exist

#this for loop checks which attributes the user wants to edit and updates them accordingly
    for i in range(len(selected_numbers)):
        if selected_numbers[i] == 1:
            if(checkIsbn(new_isbn) == True):
                return 1
            query = "update bookmanager.Book set Book.ISBN='" + new_isbn + "' where Book.ISBN='" + isbn + "'"
            isbn = new_isbn
            cursor.execute(query)
        elif selected_numbers[i] == 2:
            query = "update bookmanager.Book set Book.title='" + title + "' where Book.ISBN='" + isbn + "'"
            cursor.execute(query)
        elif selected_numbers[i] == 3:
            query = "update bookmanager.Book set Book.year='" + year + "' where Book.ISBN='" + isbn + "'"
            cursor.execute(query)
        elif selected_numbers[i] == 4:
            if(checkPublisher(published_by) == False):
                return 2  # Publisher does not exist
            query = "update bookmanager.Book set Book.published_by='" + published_by + "' where Book.ISBN='" + isbn + "'"
            cursor.execute(query)
        elif selected_numbers[i] == 5:
            if str.upper(previous_edition) != "NULL":
                query = "SELECT ISBN FROM bookmanager.Book WHERE ISBN = '" + previous_edition + "'"  # Check if the previous edition exists
                cursor.execute(query)
                results = cursor.fetchall()
                if not results:
                    return 3  # Previous edition does not exist
                query = "update bookmanager.Book set Book.previous_edition='" + previous_edition + "' where Book.ISBN='" + isbn + "'"
            else:
                query = "update bookmanager.Book set Book.previous_edition=" + "NULL" + " where Book.ISBN='" + isbn + "'"
            cursor.execute(query)
        elif selected_numbers[i] == 6:
            query = "update bookmanager.Book set Book.price='" + price + "' where Book.ISBN='" + isbn + "'"
            cursor.execute(query)

    connection.commit()
    cursor.close()
    return 4 #Book edited successfully

def checkIsbn(isbn):
# checks if a book with the specified ISBN already exists
    cursor = connection.cursor()
    query = "Select * from bookmanager.Book where Book.ISBN='" + isbn + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        return True #Book already exists
    else:
        return False

def checkPublisher(publisher):
# checks if a publisher with the specified name already exists
    cursor = connection.cursor()
    query = "Select * from bookmanager.Publisher where Publisher.name='" + publisher + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        return True #Publisher already exists
    else:
        return False