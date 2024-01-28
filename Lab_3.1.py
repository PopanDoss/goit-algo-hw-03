
import datetime as dt
from datetime import datetime as dtdt

#Отримаємо дату від користувача та сьогоднішню дату 
input_date = input("Введіть час в форматі \"РРРР-ММ-ДД\" ")
now = dtdt.now()
#створюємо функцію
def get_days_from_today() :
    try:
         #отримуємо тільки дати з поточної та введеної від користувача
         input_day_object = dtdt.strptime(input_date,"%Y-%m-%d").date() 
         today = (now.date()) 
         #отримуємо різницю дат 
         difference = (today - input_day_object)
         #Відображаємо різницю користувачу
         print(difference.days)
    except :
         return print("Не відповідає формату дати  \"РРРР-ММ-ДД\"")
#Запускаємо функцію
get_days_from_today()







