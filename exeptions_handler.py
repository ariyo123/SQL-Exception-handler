import csv
import mysql.connector as msql
from mysql.connector import Error
import datetime  
from datetime import date, timedelta
import logging
import traceback
import sys

CurrentDate=datetime.date.today()  
days = datetime.timedelta(1)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y_%m_%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 

#date = input('Please enter the date (yyyy_mm_dd):')
path=f'C:/python_work/sql_exception/exeptions/SaharaExceptions_{final_date}.log'

try:
    with open(path, 'r') as file_object:
        lines=file_object.read()
        print(f'file- SaharaExceptions_{final_date}.log exist in C:/python_work/sql_exception/exeptions/ ')
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'file- SaharaExceptions_{final_date}.log exist in C:/python_work/sql_exception/exeptions/ ') 
    #print(lines)
except:
    
    #logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.warning(f'The file does not exist in the location: {path}') 
    

else:
    contents1=lines.split('\n')
   #print(contents1)
    del contents1[-1]
    #print(contents1)
    
    try:
        conn = msql.connect(host='localhost', database='housing_data', user='root', password='Magfum12@')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logging.basicConfig(filename='log.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(f'You re connected to database: {record}') 
            print("You're connected to database: ", record)

        for line in contents1[:]:
                #print(line)  

                
            cursor.execute(line, tuple())
            #print("Record inserted/updated")
            #logging.basicConfig(filename='log.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'Record inserted/updated:{line}')
            print(f'Record inserted/updated: {line}')
                        # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
            
        #logging.basicConfig(filename='log.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(f'committed: Record(s) is/are fully updated')
        print("Record(s) is/are fully updated")  
        CurrentDate=datetime.date.today() 
    except Error as e:
            #logging.basicConfig(filename='log.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(f'Error while connecting to MySQL {CurrentDate}')
            print('Invalid connection credential')
            
            #writing in the file
           
            
      
             # closing the file
            #f.close()
   
    
   