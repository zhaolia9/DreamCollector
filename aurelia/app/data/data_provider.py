# app/data/data_provider.py

import os
import mysql.connector
from mysql.connector import Error

class DataProvider:
    def __init__(self):
        print("Connecting to DB...")
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("AURELIA_DB_PASSWORD"),
            database="aurelia"
        )
        print("Connected!")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(dictionary=True)

    # ----------------------
    # HELPER METHODS
    # ----------------------
    def _execute_commit(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.lastrowid

    def _execute_fetchone(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchone()

    def _execute_fetchall(self, query, params=None):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()

    # ======================
    # USERS
    # ======================
    def create_user(self, user):
        query = "INSERT INTO Users (name, email) VALUES (%s, %s)"
        new_id = self._execute_commit(query, (user.name, user.email))
        return self.read_user_by_id(new_id)

    def read_user_by_id(self, user_id):
        return self._execute_fetchone("SELECT * FROM Users WHERE id=%s", (user_id,))

    def read_all_users(self):
        return self._execute_fetchall("SELECT * FROM Users")

    def update_user(self, user):
        query = "UPDATE Users SET name=%s, email=%s WHERE id=%s"
        self._execute_commit(query, (user.name, user.email, user.id))
        return self.read_user_by_id(user.id)

    def delete_user(self, user_id):
        user = self.read_user_by_id(user_id)
        self._execute_commit("DELETE FROM Users WHERE id=%s", (user_id,))
        return {"deleted_user": user}

    # ======================
    # DREAMS
    # ======================
    def create_dream(self, dream):
        query = """
        INSERT INTO Dreams (user_id, title, description, date, mood, vividness)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        new_id = self._execute_commit(query, (
            dream.user_id,
            dream.title,
            dream.description,
            dream.date,
            dream.mood,
            dream.vividness
        ))
        return self.read_dream_by_id(new_id)

    def read_dream_by_id(self, dream_id):
        return self._execute_fetchone("SELECT * FROM Dreams WHERE id=%s", (dream_id,))

    def read_all_dreams(self):
        return self._execute_fetchall("SELECT * FROM Dreams")

    def update_dream(self, dream):
        query = """
        UPDATE Dreams
        SET user_id=%s, title=%s, description=%s, date=%s, mood=%s, vividness=%s
        WHERE id=%s
        """
        self._execute_commit(query, (
            dream.user_id,
            dream.title,
            dream.description,
            dream.date,
            dream.mood,
            dream.vividness,
            dream.id
        ))
        return self.read_dream_by_id(dream.id)

    def delete_dream(self, dream_id):
        dream = self.read_dream_by_id(dream_id)
        self._execute_commit("DELETE FROM Dreams WHERE id=%s", (dream_id,))
        return {"deleted_dream": dream}

    # ======================
    # SYMBOLS
    # ======================
    def create_symbol(self, symbol):
        query = "INSERT INTO Symbols (name, description) VALUES (%s, %s)"
        new_id = self._execute_commit(query, (symbol.name, symbol.description))
        return self.read_symbol_by_id(new_id)

    def read_symbol_by_id(self, symbol_id):
        return self._execute_fetchone("SELECT * FROM Symbols WHERE id=%s", (symbol_id,))

    def read_all_symbols(self):
        return self._execute_fetchall("SELECT * FROM Symbols")

    def update_symbol(self, symbol):
        self._execute_commit("UPDATE Symbols SET name=%s, description=%s WHERE id=%s",
                             (symbol.name, symbol.description, symbol.id))
        return self.read_symbol_by_id(symbol.id)

    def delete_symbol(self, symbol_id):
        symbol = self.read_symbol_by_id(symbol_id)
        self._execute_commit("DELETE FROM Symbols WHERE id=%s", (symbol_id,))
        return {"deleted_symbol": symbol}

    # ======================
    # POEMS
    # ======================
    def create_poem(self, poem):
        query = "INSERT INTO Poems (author_id, dream_id, content, created_at) VALUES (%s,%s,%s,%s)"
        new_id = self._execute_commit(query, (
            poem.author_id,
            poem.dream_id,
            poem.content,
            poem.created_at
        ))
        return self.read_poem_by_id(new_id)

    def read_poem_by_id(self, poem_id):
        return self._execute_fetchone("SELECT * FROM Poems WHERE id=%s", (poem_id,))

    def read_all_poems(self):
        return self._execute_fetchall("SELECT * FROM Poems")

    def update_poem(self, poem):
        self._execute_commit("UPDATE Poems SET author_id=%s,dream_id=%s,content=%s,created_at=%s WHERE id=%s",
                             (poem.author_id, poem.dream_id, poem.content, poem.created_at, poem.id))
        return self.read_poem_by_id(poem.id)

    def delete_poem(self, poem_id):
        poem = self.read_poem_by_id(poem_id)
        self._execute_commit("DELETE FROM Poems WHERE id=%s", (poem_id,))
        return {"deleted_poem": poem}

    # ======================
    # DREAM SYMBOLS (MANY-TO-MANY)
    # ======================
    def create_dream_symbol(self, dream_symbol):
        self._execute_commit(
            "INSERT INTO DreamSymbols (dream_id, symbol_id) VALUES (%s,%s)",
            (dream_symbol.dream_id, dream_symbol.symbol_id)
        )
        return self.read_dream_symbol_by_id(dream_symbol.dream_id, dream_symbol.symbol_id)

    def read_dream_symbol_by_id(self, dream_id, symbol_id):
        return self._execute_fetchone(
            "SELECT * FROM DreamSymbols WHERE dream_id=%s AND symbol_id=%s",
            (dream_id, symbol_id)
        )

    def read_all_dream_symbols(self):
        return self._execute_fetchall("SELECT * FROM DreamSymbols")

    def read_dream_symbols_by_dream(self, dream_id):
        return self._execute_fetchall(
            "SELECT s.* FROM Symbols s JOIN DreamSymbols ds ON s.id = ds.symbol_id WHERE ds.dream_id=%s",
            (dream_id,)
        )

    def read_dream_symbols_by_symbol(self, symbol_id):
        return self._execute_fetchall(
            "SELECT d.* FROM Dreams d JOIN DreamSymbols ds ON d.id = ds.dream_id WHERE ds.symbol_id=%s",
            (symbol_id,)
        )

    def update_dream_symbol(self, dream_id, old_symbol_id, new_symbol_id):
        self._execute_commit(
            "UPDATE DreamSymbols SET symbol_id=%s WHERE dream_id=%s AND symbol_id=%s",
            (new_symbol_id, dream_id, old_symbol_id)
        )
        return self.read_dream_symbol_by_id(dream_id, new_symbol_id)

    def delete_dream_symbol(self, dream_id, symbol_id):
        link = self.read_dream_symbol_by_id(dream_id, symbol_id)
        self._execute_commit("DELETE FROM DreamSymbols WHERE dream_id=%s AND symbol_id=%s",
                             (dream_id, symbol_id))
        return {"deleted_link": link}

    # ----------------------
    # CLOSE CONNECTION
    # ----------------------
    def close(self):
        if self.connection.is_connected():
            self.connection.close()