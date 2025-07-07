import sqlite3
import bcrypt # pip install bcrypt

class DatabaseManager:
    def __init__(self, db_name="user_data.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._create_tables()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            # You might want to raise an exception or handle this more gracefully
            raise

    def _create_tables(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone_number TEXT,
                    country TEXT,
                    password_hash TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            raise

    def register_user(self, full_name, email, phone_number, country, password):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self.cursor.execute(
                "INSERT INTO users (full_name, email, phone_number, country, password_hash) VALUES (?, ?, ?, ?, ?)",
                (full_name, email, phone_number, country, hashed_password)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # This means the email already exists
            return False
        except sqlite3.Error as e:
            print(f"Error registering user: {e}")
            return False

    def verify_user(self, email, password):
        try:
            self.cursor.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
            result = self.cursor.fetchone()
            if result:
                stored_password_hash = result[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8'))
            return False
        except sqlite3.Error as e:
            print(f"Error verifying user: {e}")
            return False

    def get_user_info(self, email):
        try:
            self.cursor.execute("SELECT full_name, email, phone_number, country FROM users WHERE email = ?", (email,))
            return self.cursor.fetchone() # Returns a tuple (full_name, email, phone, country) or None
        except sqlite3.Error as e:
            print(f"Error retrieving user info: {e}")
            return None

    def close(self):
        if self.conn:
            self.conn.close()