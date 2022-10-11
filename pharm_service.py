import json
from db_manager import mysql
class PharmService:
    
    def __init__(self):
        self.mysql = mysql;

    def find(self,id):
        q = "SELECT * FROM tpharm WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data
    
    def delete(self,id):
        q = "delete FROM tpharm WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()