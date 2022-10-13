import json
from db_manager import mysql
class BoxService:
    
    def __init__(self):
        self.mysql = mysql;

    def find(self,id):
        """
        Restituisce un box tramite id
        """
        q = "SELECT * FROM tbox WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def create(self,idpharm,number,color,message,timebox,delta):
        """
        Crea un box per la pharm
        """
        q = "insert into tbox (idpharm,number,color,message,timebox,deltatime) VALUES ('%s','%s','%s','%s','%s','%s')" % (idpharm,number,color,message,timebox,delta)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)   

    def delete(self,id):
        """
        Elimina un box tramite id
        """
        q = "delete FROM tbox WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def deleteByPharm(self,idpharm):
        """
        Elimina tutti i boxes della pharm
        """
        q = "delete FROM tbox WHERE idpharm = " + str(idpharm)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def boxesByPharm(self, idpharm):
        """
        Restituisce i boxes della pharm
        """
        q = "select * from tbox where idpharm = " + str(idpharm)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data

    def boxesByPharmForArduino(self, macaddress):
        """
        Restituisce i boxes della pharm tramite macaddress
        """
        q = "select b.* from tbox b inner join tpharm p on b.idpharm = p.id  where p.macaddress = '%s'" % (macaddress)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data