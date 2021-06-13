from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from url_test import *
from config import *
import pymysql
import warnings
import time


warnings.filterwarnings("ignore")
# Defining program to run
#Url page that needs to be scrapped

def page_links():

    db= pymysql.connect(**config)
    cursor = db.cursor()
    
    sql= """ CREATE TABLE IF NOT EXISTS links (
            url   CHAR(255))"""
    cursor.execute(sql)
    db.commit()
        # Create table as per requirement
   
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    url_page= url_ok()
    
    driver_1 = webdriver.Chrome(chrome_options=options, executable_path=r'D:/gmachine/chromedriver.exe')
    
    pages=[]   
    
    i= 0
    while True:
        i += 1    
        url= url_page + "?page={}".format(str(i))

        url1 =requests.get(url)
        if url1.status_code == 404:
            break
        else:
            driver_1.get(url)
            
            elements = driver_1.find_elements_by_xpath("//p[@class='text-primary font-semibold mr-5 text-lg']//a")
            
            for element in elements:        
                x=element.get_attribute("href")
               
                cursor.execute("SELECT url FROM links WHERE url= %s",
                                (x,))
                results= cursor.fetchone()
                
                if results is None:
                    
                    mySql_insert_query1 = """INSERT INTO links (url) 
                                        VALUES (%s)"""
                    cursor.execute(mySql_insert_query1,(x))
                    db.commit()
                    
                else:
                    continue
          