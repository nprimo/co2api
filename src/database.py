import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Database(object):
	def __init__(self, dbname):
		self.dbname = dbname
		self.cursor = None
		self.conn = None
		
	def connDB(self):
		self.conn = mysql.connector.connect(
			database=os.getenv("DB_NAME"),
			host=os.getenv("DB_HOST"),
			port=int(os.getenv("DB_PORT")),
			user=os.getenv("DB_USER"),
			password=os.getenv("DB_PASSWORD")
		)
		self.cursor = self.conn.cursor()
		
	def createDB(self):
		self.connDB()
		self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS co2data (
            id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            countryCode VARCHAR(6) NOT NULL,
            datetime VARCHAR(30) NOT NULL,
            carbonIntensity FLOAT NOT NULL,
			unit VARCHAR(10) NOT NULL,
			UNIQUE (datetime)
			)
            '''
        )
		self.conn.commit()
		self.conn.close()
	
	def queryDB(self, sql):
		self.connDB()
		self.cursor.execute(sql)
		if sql[:6].lower() == 'select':
			result = self.cursor.fetchall()
			self.conn.close()
			return result
		else:
			self.conn.commit()
			self.conn.close()
