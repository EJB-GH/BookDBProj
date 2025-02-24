import psycopg2


class connect():
    def __init__(self):
        self.db_name = "postgres"
        self.db_user = "postgres"
        self.db_password = "711984BerryRydell9"
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
