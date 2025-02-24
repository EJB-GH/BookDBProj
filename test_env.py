import psycopg2

db_name = "postgres"
db_user = "postgres"
db_password = "711984BerryRydell9"
db_host = "localhost"
db_port = "5432"
db_options = "-c search_path=dev_env"

try:
    connection = psycopg2.connect(
        database = db_name,
        user = db_user,
        password = db_password,
        host = db_host,
        port = db_port,
        options = db_options
    )
    print("Connected to Database.")

except psycopg2.Error as error:
    print(f"Error in connecting to database: {error}")

'''
def all_books(connection):
    with connection as db:
        with db.cursor() as cur:
            cur.execute("select * from books")
            result = cur.fetchall()

            print("Books Table: \n")
            print(cur.rowcount, " total entries.\n")
            for row in rows:
                print(row)
'''

with connection as db:
        with db.cursor() as cur:
            cur.execute("select * from books")
            result = cur.fetchall()

            print("Books Table: \n")
            print(cur.rowcount, "total entries.\n")
            for row in result:
                print(row)

#def total_books(self):
        '''
        as it sounds, this returns the amount of books
        held in the lirary
        '''
with db.cursor() as query:
    query.execute('select count(books.id) Books from books')
    result = query.fetchone()
    
    print("Total number of books: ", result[0])

if connection:
    connection.close()
    print("Connection ended...")

