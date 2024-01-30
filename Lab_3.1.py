
import datetime as dt
from datetime import datetime as dtdt

#Отримаємо дату від користувача та сьогоднішню дату 
input_date = input("Введіть час в форматі \"РРРР-ММ-ДД\" ")

#створюємо функцію
def get_days_from_today(input_date: str) :
    try:
         #отримуємо тільки дати з поточної та введеної від користувача
         input_day_object = dtdt.strptime(input_date,"%Y-%m-%d").date()
         now = dtdt.now()
         today = (now.date()) 
         #отримуємо різницю дат 
         difference = (today - input_day_object)
         #Повертаємо різницю користувачу
         return (difference.days)
    except :
         print("Не відповідає формату дати  \"РРРР-ММ-ДД\"")

# відображаємо, щоб побачити результат роботи функції.
print (get_days_from_today(input_date))







