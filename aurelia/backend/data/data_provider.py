from datetime import datetime
from ..db import get_connection
from backend.models import User, Dream, Symbol, DreamSymbol, Poem

class DataProvider:
    def __init__(self):
        self.conn = get_connection()

    # ---------- USERS ----------
    def create_user(self, user: User) -> int:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Users (name, email) VALUES (%s, %s)", (user.name, user.email))
        self.conn.commit()
        return cur.lastrowid

    def read_user_by_id(self, user_id: int):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Users WHERE id=%s", (user_id,))
        return cur.fetchone()

    def read_all_users(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Users")
        return cur.fetchall()

    def update_user(self, user: User):
        cur = self.conn.cursor()
        cur.execute("UPDATE Users SET name=%s, email=%s WHERE id=%s", (user.name, user.email, user.id))
        self.conn.commit()

    def delete_user(self, user_id: int):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Users WHERE id=%s", (user_id,))
        self.conn.commit()

    # ---------- DREAMS ----------
    def create_dream(self, dream: Dream) -> int:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO Dreams (user_id, title, description, date, mood, vividness)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (dream.user_id, dream.title, dream.description, dream.date, dream.mood, dream.vividness))
        self.conn.commit()
        return cur.lastrowid

    def read_dream_by_id(self, dream_id: int):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Dreams WHERE id=%s", (dream_id,))
        return cur.fetchone()

    def read_all_dreams(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Dreams")
        return cur.fetchall()

    def update_dream(self, dream: Dream):
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE Dreams SET user_id=%s, title=%s, description=%s, date=%s, mood=%s, vividness=%s
            WHERE id=%s
        """, (dream.user_id, dream.title, dream.description, dream.date, dream.mood, dream.vividness, dream.id))
        self.conn.commit()

    def delete_dream(self, dream_id: int):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Dreams WHERE id=%s", (dream_id,))
        self.conn.commit()

    # ---------- SYMBOLS ----------
    def create_symbol(self, symbol: Symbol) -> int:
        cur = self.conn.cursor()
        cur.execute("INSERT INTO Symbols (name, description) VALUES (%s, %s)", (symbol.name, symbol.description))
        self.conn.commit()
        return cur.lastrowid

    def read_symbol_by_id(self, symbol_id: int):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Symbols WHERE id=%s", (symbol_id,))
        return cur.fetchone()

    def read_all_symbols(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Symbols")
        return cur.fetchall()

    def update_symbol(self, symbol: Symbol):
        cur = self.conn.cursor()
        cur.execute("UPDATE Symbols SET name=%s, description=%s WHERE id=%s", (symbol.name, symbol.description, symbol.id))
        self.conn.commit()

    def delete_symbol(self, symbol_id: int):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Symbols WHERE id=%s", (symbol_id,))
        self.conn.commit()

    # ---------- DREAMSYMBOLS ----------
    def create_dream_symbol(self, ds: DreamSymbol):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO DreamSymbols (dream_id, symbol_id) VALUES (%s, %s)", (ds.dream_id, ds.symbol_id))
        self.conn.commit()

    def read_all_dream_symbols(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM DreamSymbols")
        return cur.fetchall()

    def delete_dream_symbol(self, dream_id: int, symbol_id: int):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM DreamSymbols WHERE dream_id=%s AND symbol_id=%s", (dream_id, symbol_id))
        self.conn.commit()

    # ---------- POEMS ----------
    def create_poem(self, poem: Poem) -> int:
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO Poems (author_id, dream_id, content, created_at)
            VALUES (%s, %s, %s, %s)
        """, (poem.author_id, poem.dream_id, poem.content, poem.created_at))
        self.conn.commit()
        return cur.lastrowid

    def read_poem_by_id(self, poem_id: int):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Poems WHERE id=%s", (poem_id,))
        return cur.fetchone()

    def read_all_poems(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM Poems")
        return cur.fetchall()

    def update_poem(self, poem: Poem):
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE Poems SET author_id=%s, dream_id=%s, content=%s, created_at=%s
            WHERE id=%s
        """, (poem.author_id, poem.dream_id, poem.content, poem.created_at, poem.id))
        self.conn.commit()

    def delete_poem(self, poem_id: int):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM Poems WHERE id=%s", (poem_id,))
        self.conn.commit()
