import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        
    #def find_by_username(self, username):
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor =  connection.cursor()
        query = "SELECT * FROM USERS WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            #user = User(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None
            
        connection.close()
        
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor =  connection.cursor()
        query = "SELECT * FROM USERS WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            #user = User(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None
            
        connection.close()