import json
from db_manager import mysql
class BoxlogService:
    
    def __init__(self):
        self.mysql = mysql;

    def find(self,id):
        """
        Restituisce un boxlog tramite id
        """
        q = "SELECT * FROM tboxlog WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def create(self,idbox,status,delta):
        """
        Crea un boxlog per il box
        """
        q = "insert into tboxlog (idbox,status,delta) VALUES ('%s','%s','%s')" % (idbox,status,delta)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)   

    def delete(self,id):
        """
        Elimina un boxlog tramite id
        """
        q = "delete FROM tboxlog WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def deleteByBox(self,idbox):
        """
        Elimina tutti i boxlog del box
        """
        q = "delete FROM tboxlog WHERE idbox = " + str(idbox)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def logByBox(self, idbox):
        """
        Restituisce i log del box
        """
        q = "select * from tboxlog where idbox = " + str(idbox)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data
