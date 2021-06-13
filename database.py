import pymysql
from scrape_data import *
from config import *


def database():
  cnx = pymysql.connect(**config)

  # create cursor to execute mysql commands
  cursor = cnx.cursor()

  # Now create table like this one
  cursor.execute("DROP TABLE IF EXISTS Land")


  # Create table as per requirement
  sql= """ CREATE TABLE land (
      Place CHAR(255),
      Size  CHAR(50),
      Price   CHAR (255),
      url   CHAR(255))"""
  cursor.execute(sql)

  cnx = pymysql.connect(**config)
  mySql_insert_query = """INSERT INTO land (Place,Size,Price,url) 
  VALUES (%s, %s, %s, %s)"""

  records_to_insert = scrape()
  cursor = cnx.cursor()
  cursor.executemany(mySql_insert_query, records_to_insert)
  
  cnx.commit()
  print(cursor.rowcount, "Record inserted successfully into land table")
  