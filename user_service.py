import json
from db_manager import mysql
from pharm_service import PharmService

class UserService:

    def __init__(self):
        self.mysql = mysql;
        self.pharmService = PharmService()

    def all(self):
        q = "SELECT * FROM tuser order by usr"
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data
    
    def find(self,id):
        q = "SELECT * FROM tuser WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def create(self,usr,pwd,firstname,lastname,email):
        q = "INSERT INTO tuser (usr,pwd,firstname,lastname,email) VALUES ('%s','%s','%s','%s','%s')" % (usr,pwd,firstname,lastname,email)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)

    def delete(self,id):
        q = "delete FROM tuser WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        
    def pharms(self,id):
        q = "SELECT * FROM tpharm WHERE iduser = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall();
        return data

    def createPharm(self,id,name,ip,macaddress,wiocode,accesspoint,password,gmt):
        q = "INSERT INTO tpharm (iduser,name,ip,macaddress,wiocode,accesspoint,password,gmt) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (id,name,ip,macaddress,wiocode,accesspoint,password,gmt)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.pharmService.find(lastid)