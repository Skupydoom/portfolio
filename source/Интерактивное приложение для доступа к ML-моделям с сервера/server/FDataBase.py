import sqlite3
from time_now import RequestTimeFromNtp


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
    
    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Error while reading data from the database")
        return []
    
    def addUser(self, email, hspw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res["count"] > 0:
                print("User with such email already exists")
                return False
            
            tm = RequestTimeFromNtp()
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?)", (email, hspw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error while adding the user into the database" + str(e))
            return False
        
        return True
    
    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False
            
            return res
        except sqlite3.Error as e:
            print("Error while getting data from the database " + str(e))
        
        return False
    
    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False
            
            return res
        except sqlite3.Error as e:
            print("Error while getting data from the database " + str(e))
        
        return False
