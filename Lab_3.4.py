import datetime as dt
from datetime import datetime as dtdt

#список словників, що будемо перетворювати
users = [
    {"name": "John Doe", "birthday": "1991.03.29"},
    {"name": "Jane Smith", "birthday": "1990.01.29"}
]

#Створюємо функцію
def get_upcoming_birthdays(users):
    #Створюємо список який будемо наповнювати
    upcoming_birthdays = []
    # Визначаємо дату сьогодні
    today = dtdt.today().date()
    #перебираємо значення для кожного словнику в списку
    for user in users:
        #отрисуємо дату для данної ітерації, переводимо в рядок та заначаємо дійсний рік, переводимо в рядок datetime
        birthday = user["birthday"]
        birthday = str(today.year)+birthday[4:]
        birthday_this_year = dtdt.strptime(birthday, "%Y.%m.%d").date()        
        #Перевіряємо чи отримана дата вже відбулась
        if birthday_this_year < today:
            pass
        #Перевіряємо, чи відбудеться наступні сім днів 
        else:
            different_day = (birthday_this_year - today).days
            if 7>= different_day>=0:
                #Якщо так, визначаємо який це день тижня
                day_in_week = birthday_this_year.isoweekday()
                #Змінюємо дату на понеділок,якщо вона потрапляєна вихідні, та додаємо словником у список
                if day_in_week <6 :
                    upcoming_birthdays.append({"name":user["name"], "birthday": birthday})
                elif day_in_week == 6:
                    upcoming_birthdays.append({"name":user["name"], "birthday": (birthday_this_year + dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                else :
                    upcoming_birthdays.append({"name":user["name"], "birthday": (birthday_this_year + dt.timedelta(days=1)).strftime("%Y.%m.%d")})
    #Повертаємо відображення отриманих словників в списку
    return print(upcoming_birthdays) 

#викликаємо функцію
get_upcoming_birthdays(users)


