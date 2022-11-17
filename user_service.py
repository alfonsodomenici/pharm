import json
from db_manager import mysql

class UserService:

    def __init__(self):
        self.mysql = mysql;


    def all(self):
        """
        Restiruisce tutti gli users
        """
        q = "SELECT * FROM tuser order by usr"
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data
    

    def find(self,id):
        """
        Restutuisce uno user tramite id
        """
        q = "SELECT * FROM tuser WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data


    def create(self,usr,pwd,firstname,lastname,email):
        """
        Crea uno user
        """
        q = "INSERT INTO tuser (usr,pwd,firstname,lastname,email) VALUES ('%s','%s','%s','%s','%s')" % (usr,pwd,firstname,lastname,email)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)


    def delete(self,id):
        """
        Elimina uno user tramite id
        """
        q = "delete FROM tuser WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        
    def findByUsrPwd(self,usr,pwd):
        """
        Restutuisce uno user tramite usr e pwd
        """
        q = "SELECT * FROM tuser WHERE usr = '%s' and pwd = '%s' " % (usr,pwd)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data