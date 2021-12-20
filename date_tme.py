import datetime  
from datetime import date, timedelta
CurrentDate=datetime.date.today()  
#%d is for date  
#%b is for month  
#Y is for Year  
print(CurrentDate.strftime('%Y_%m_%d'))  


dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)