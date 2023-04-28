from cmath import sqrt
import datetime

# 1 Простейшие арифметические операции

def arithmetic(num1,num2,operation):
    '''Функция, принимающая 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
    Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). 
    В остальных случаях вернуть строку "Неизвестная операция". '''

    if operation == '+':
        result = num1 + num2
    elif operation =='-':
        result = num1 - num2
    elif operation =='*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = print("Деление на ноль невозможно")
        else:        
            result = num1/num2
    else:
        print("Неизвестная операция!")
        arithmetic(2,5,'+')
    return result



# 2 Високосный год

def is_year_leap(year):
    '''Функция проверяет год високосный или нет'''

    if (year % 400 == 0) and (year % 100 == 0):
        print(year,"- високосный год")
        answer = True

    elif (year % 4 ==0) and (year % 100 != 0):
        print(year,"- високосный год")
        answer = True

    else:
        print(year, "- не високосный год")
        answer = False
    return answer



# 3 Квадрат

def square (side):
    '''Функция, принимает 1 аргумент — сторону квадрата, и возвращает 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.'''
    P = side*4
    S = side * side
    D = side*sqrt(2)

    return P, S, D
    


# 4 Времена года

def season(monthNumber:int):
    """Функцию принимает 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis)."""
    
    if monthNumber == 12:
        a = "Talv"
    elif monthNumber == 1:
        a = "Talv"
    elif monthNumber == 2:
        a = "Talv"
    elif monthNumber == 3:
        a = "Kevad"
    elif monthNumber == 4:
        a = "Kevad"
    elif monthNumber == 5:
        a = "Kevad"
    elif monthNumber == 6:
        a = "Suvi"
    elif monthNumber == 7:
        a = "Suvi"
    elif monthNumber == 8:
        a = "Suvi"
    elif monthNumber == 9:
        a = "Sügis"
    elif monthNumber == 10:
        a = "Sügis"
    elif monthNumber == 11:
        a = "Sügis"
    else:
        a = "Неправильный номер месяца!"
    return a



# 5 Банковский вклад

def bank(a: int, years: int):
    '''Функция запрашивает сумму вклада и количство лет, на которое делается вклад. Возвращает сумму вместе с процентными накоплениями.'''

    i= 0  
    #a = int(input("Сумма вклада: "))
    #years = int(input("Введите количество лет, на которое делается вклад: "))
    
    for i in range(years):
        
        savings = a*0.1+a
        a = savings
    
        i+1

    print(f"Ваши сбережения: {round(savings,2)} евро")

    return round(savings,2)



# 6 Простые числа

def is_prime(number: int):
    ''' Функция проверяет введенные числа от 0 до 1000, являются ли они простыми или нет. Возвращает True, если оно простое, и False - если составное.'''

    if number == 0 or number == 1:
        print(f"{number} не является ни простым, ни составным числом.")
        answer = False

    elif number == 2:
                    print(f"Число {number} - простое")
                    answer = True

    elif number > 0 and number < 1000:
            d = 2
            while number % d != 0:
                d += 1
                               
                if d==number:
                    print(f"Число {number} - простое")
                    answer = True        

            if d < number:
                print(f"Число {number} - составное")
                answer = False
    else:
        print("Введите число от 0 до 1000.")
        
    return answer



# 7 Правильная дата

def date():
    '''Функция показывает текущую правилную дату'''
    
    x = datetime.datetime.now()

    return x
