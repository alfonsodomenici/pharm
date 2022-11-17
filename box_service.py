import json
from db_manager import mysql
from flask import request
class BoxService:
    
    def __init__(self):
        self.mysql = mysql

    def find(self,id):
        """
        Restituisce un box tramite id
        """
        q = "SELECT *, date_format(now(),'%H:%i:%s') as ora,if( TIMEDIFF(date_format(now(), '%H:%i:%s '), timebox) >time(concat( '00: ',deltatime, ':00 ')) ,1,0) as oltre,if( TIMEDIFF(date_format(now(), '%H:%i:%s '), timebox) <-time(concat( '00: ',deltatime, ':00 ')) ,1,0) as prima FROM tbox WHERE id = " + str(id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def create(self,idpharm,number,color,message,timebox,deltatime):
        """
        Crea un box per la pharm
        """
        q = "insert into tbox (idpharm,number,color,message,timebox,deltatime) VALUES ('%s','%s','%s','%s','%s','%s')" % (idpharm,number,color,message,timebox,deltatime)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)

    def update(self, id,number,color,message,timebox,deltatime):
        """
        Aggiorna un box
        """
        q = "UPDATE tbox SET number='%s', color='%s', message='%s', timebox='%s', deltatime='%s' WHERE id = %s" % (number,color,message,timebox,deltatime,id)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()   
        return self.find(id)

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
        q = "select *, date_format(now(),'%H:%i:%s') as ora,if( TIMEDIFF(date_format(now(), '%H:%i:%s '), timebox) >time(concat( '00: ',deltatime, ':00 ')) ,1,0) as oltre,if( TIMEDIFF(date_format(now(), '%H:%i:%s '), timebox) <-time(concat( '00: ',deltatime, ':00 ')) ,1,0) as prima from tbox where idpharm = " + str(idpharm)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data

    def boxesByPharmForArduino(self, macaddress):
        """
        Restituisce i boxes della pharm tramite macaddress
        """
        q = "select b.*, date_format(now(),'%H:%i:%s') as ora,if( TIMEDIFF(date_format(now(), '%H:%i:%s'), timebox) >time(concat( '00: ',deltatime, ':00 ')) ,1,0) as oltre,if( TIMEDIFF(date_format(now(), '%H:%i:%s'), timebox) <-time(concat( '00: ',deltatime, ':00 ')) ,1,0) as prima from tbox b inner join tpharm p on b.idpharm = p.id  where p.macaddress = '" + macaddress + "'"
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data