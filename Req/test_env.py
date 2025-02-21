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

if connection:
    connection.close()
    print("Connection ended...")

