import sqlite3

sqlite3_db_file_name = 'pinglog-sqlite3.db'
db_table_name = 'pinglog'

class DB:
    def __init__(self):
        self.conn = sqlite3.connect(sqlite3_db_file_name)

        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS {db_table_name}(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    date TEXT,
                    dest TEXT,
                    ping TEXT
                )
            """.format(db_table_name=db_table_name))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def insert(self, date, dest, ping):
        with self.conn as conn:
            cursor = conn.cursor()
            data = {"date" : date, "dest" : dest, "ping" : ping}
            cursor.execute("""
                INSERT INTO {db_table_name}(date, dest, ping) VALUES(:date, :dest, :ping)""".format(
                    db_table_name=db_table_name),
                data)

