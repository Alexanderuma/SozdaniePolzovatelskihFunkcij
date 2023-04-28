from myModule import*


## Ответы
# 1 Простейшие арифметические операции
answer = arithmetic(2,5,'+')
print("Ответ в случае, arithmetic(2,5,'+') равен: ",answer)

answer = arithmetic(2,5,'-')
print("Ответ в случае, arithmetic(2,5,'-) равен: ",answer)

answer = arithmetic(2,5,'*')
print("Ответ в случае, arithmetic(2,5,'*') равен: ",answer)

answer = arithmetic(2,5,'/')
print("Ответ в случае, arithmetic(2,5,'/') равен: ",answer)

answer = arithmetic(2,0,'/')
print("Ответ в случае, arithmetic(2,0,'/') равен: ",answer)
print()



## Ответ
# 2 Високосный год
a = is_year_leap(2000)
print(a)
print()



## Ответ
# 3 Квадрат
b = square(3)
print(b)
print()



## Ответ
# 4 Времена года
a = season(11)
print(a)
print()



## Ответ
# 5 Банковский вклад
money = bank(1000, 10)
print(money)
print()



## Ответ
# 6 Простые числа
num = is_prime(907)
print(num)
print()



## Ответ
# 7 Правильная дата
a = date()
print("Правилная дата:",a)