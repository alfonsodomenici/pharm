import json
from db_manager import mysql
class PharmService:
    
    def __init__(self):
        self.mysql = mysql;

    def find(self,id):
        """
        Restituisce una pharm tramite id
        """
        q = "SELECT * FROM tpharm WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data
    
    def delete(self,id):
        """
        Elimina una pharm tramite id
        """
        q = "delete FROM tpharm WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def pharmsByUser(self,iduser):
        """
        Restituisce tutte le pharms dello user
        """
        q = "SELECT * FROM tpharm WHERE iduser = " + str(iduser)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall();
        return data

    def create(self,iduser,name,ip,macaddress,wiocode,accesspoint,password,gmt):
        """
        Crea una pharm per lo user
        """
        q = "INSERT INTO tpharm (iduser,name,ip,macaddress,wiocode,accesspoint,password,gmt) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (iduser,name,ip,macaddress,wiocode,accesspoint,password,gmt)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)

