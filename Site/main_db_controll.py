import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    
    def init_table(self):
        self.open()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, email TEXT, message TEXT)''')
        self.close()

    def get_data(self):
        self.open()
        self.cursor.execute(
            '''SELECT * FROM users'''
            )
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def add_data(self, info):
        self.open()
        
        self.cursor.execute('''INSERT INTO users (name, email, message) VALUES (?, ?, ?)''', info)
        self.conn.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()

db = DB_Controller('question.db')
db.init_table()