from config import *
import pymysql
from page_links import *


db= pymysql.connect(**config)

# create cursor to execute mysql commands
cursor = db.cursor()
   # Now create table like this one
cursor.execute("DROP TABLE IF EXISTS links")
# Create table as per requirement
sql= """ CREATE TABLE links (
      url   CHAR(255))"""
cursor.execute(sql)
db = pymysql.connect(**config)
mySql_insert_query1 = """INSERT INTO land (url) 
  VALUES (%s)"""

records_to_insert1 = pages
cursor = db.cursor()
cursor.executemany(mySql_insert_query1, records_to_insert1)
  
db.commit()