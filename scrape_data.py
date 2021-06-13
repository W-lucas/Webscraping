from selenium import webdriver
from time import sleep
from page_links import *
from database import *
from config import *
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

def diff(results,results1):
    out=[i for i in results1 if not i in results]
    return out



# Defining program to run
# Querying page links from db
def scrape():
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    driver= webdriver.Chrome(chrome_options=options, executable_path=r'D:/gmachine/chromedriver.exe')
    
    db= pymysql.connect(**config)
    
    cursor=db.cursor()
    cursor1=db.cursor()
    # query links from table land
    cursor.execute("SELECT url FROM land")
    cursor1.execute("SELECT url FROM links")
    results=cursor.fetchall()
    
    results1= cursor1.fetchall()
    
    m= diff(results,results1)
    
    if m:
    
        for j in m:
            print(j[0]) 
            driver.get(j[0])
            
            place=driver.find_element_by_xpath("//p[@data-cy='listing-address']")
            size= driver.find_element_by_xpath("//div[@data-cy='listing-basic-details-list']")
            price=driver.find_element_by_xpath("//span[@class='text-xl font-bold block mr-3']")
            sleep(5)
            
            cursor2=db.cursor()
            
    # Create table as per requirement
            sql= """ CREATE TABLE IF NOT EXISTS land (
                Place CHAR(255),
                Size  CHAR(50),
                Price   CHAR (255),
                url   CHAR(255))"""
            cursor2.execute(sql)
            # inserting data to mysql data base
            mySql_insert_query = """INSERT INTO land (Place,Size,Price,url) 
                                VALUES (%s, %s, %s, %s)"""

            
            cursor2.execute(mySql_insert_query,(place.text,size.text,price.text,j))
            db.commit()
            print(cursor2.rowcount, "Record inserted successfully into land table")
    else:
        
        pass
    driver.close()
    