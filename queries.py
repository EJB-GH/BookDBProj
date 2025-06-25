import psycopg2

#running the python insert is actually much slower than running
#\copy in the sql functions, should test this when testing this program
#to see how it performs on a much smaller load amount, and on my own machine

class connect():
    def __init__(self):
        self.db_name = "postgres"
        self.db_user = "postgres"
        self.db_password = ""
        self.db_host = "localhost"
        self.db_port = "5432"
        self.db_options = "-c search_path=dev_env"
        self.db = self.connection()

    def connection(self):
        try:
            connection = psycopg2.connect(
                database = self.db_name,
                user = self.db_user,
                password = self.db_password,
                host = self.db_host,
                port = self.db_port,
                options = self.db_options
            )
            print("Connected to Database.")
        except psycopg2.Error as error:
            print(f"Error in connecting to database: {error}")

        return connection

class query(connect):
    
    def __init__(self, connection):
        self.db = connection


    def display(self):
        '''
        makes more sense to house all returns into a display statement that strips
        the db tuple formatting and makes it look nice
        '''


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

    def search_author(self):
        '''
        function allows searching of the database
        for specific authors and their output
        BY AUTHOR_FIRST AUTHOR_LAST
        Uses the str_input function
        '''
        print("Author First name: ")
        first_name = name_input()
        print("Author Last name: ")
        last_name = name_input()
        #keeping this seperate to compare against entries in the database 

        with self.db.cursor() as query:
            #need to look over database structure before finalizing this query
            query.execute("""
                select books.titles 
                from books
                join authors on books.author_id = authors.id
                where author.first = %(first_name)s 
                and author.last = %(last_name)s
                """, 
                {'first_name': first_name, 'last_name': last_name}
            )

        result = query.fetchall()
        if result is None:
            print('No results')
            return False
        
        return result

    def search_series(self):
        '''
        function allows searching of the database
        for a specific series
        BY SERIES
        '''
        pass

    def search_book(self):
        '''
        function allows searching of the database
        for single book existence
        BY TITLE
        '''
        pass
            

        

