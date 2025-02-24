from connection import *

class query(connection):
    def __init__(self, connection):
        self.db = connection


    def total_books(self):
        '''
        as it sounds, this returns the amount of books
        held in the lirary
        '''
        with self.db.cursor() as query:
            query.execute('select count(books.id) Books from books')
            result = query.fetchone()
 
            #learned that psycopg returns tuples
            print("Total number of books: ", result[0])

    
            

        

