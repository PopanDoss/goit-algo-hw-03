import random 

# Приймаємо значення, що ввів користувач 
min = (input("Ведіть мінімальне число в діапазоні від 1 до 1000: "))
max = (input("Ведіть максимальне число в діапазоні від 1 до 1000: "))
quantity = (input("Вкажіть кількість чисел в виграшній комбінації: "))

#Створює функцію, що згенерує виграшну комбінацію
def get_numbers_ticket(min, max, quantity):
    win_list =[]
    try:
        #Переводимо значення в числові в середині функції, щоб спіймати помилку,якщо користувач ввів букви/символи  
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        # перевіряємо, чи відповідають умовам введені користувачем дані
        if (min >= 1) and (max <= 1000) and (min < max) and (0< quantity <= max):
            #Генеруємо виграшну комбінацію
            while len(win_list) < quantity:
                win_number = random.randrange(min,max)
                if win_number not in win_list:
                    win_list.append(win_number)
                else:
                    continue
                #Сортуємо виграшну комбінацію від найменшого до найбільшого
            win_list = sorted(win_list)
            #Повертаємо значення, та виводимо на екран:
            return print(f"Виграшна комбінація: \n{win_list}")       
        else:
            print("Вказані параметри не відповідають вимогам")
            return win_list
    except:
        print("Будь ласка, введіть цілі числа!")


#Виклакаємо функцію
get_numbers_ticket(min,max,quantity)
