import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]



#створюємо функцію для перетворення номерів 
def normalize_phone(num) : 
    #створимо змінну, куди запишемо відредагований номер
    correct_value_number = () 
    #отримуємо тільки числові значення номеру в форматі рядку 
    pattern = r"[\d]+"
    only_numbers = " ".join(re.findall(pattern, num))
    only_numbers = only_numbers.replace(" ", "")
    #Якщо кілкість цифр в номері 10 додаємо "+380", якщо 12 додаємо "+"
    if len(only_numbers) == 10 :
        normal_number = "+38" + only_numbers
        
    elif len (only_numbers) == 12 :
        normal_number = "+" + only_numbers
        
    else:
        print("Некорректно введені номери ")
    #отриманий рядок записуємо в писок та повертаємо його
    correct_value_number = normal_number
    return correct_value_number
    


sanitized_number = [normalize_phone(num) for num in raw_numbers]
# Виводимо список відредагованих елементів на екран
print("Нормалізовані номери телефонів для SMS-розсилки: ", sanitized_number)
