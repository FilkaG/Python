print('************ Задание 1 ***********')
number=10
string='My first homework'
print('число - ',number)
print('строка - ',string)
string_2=input('введите любое предложение: ')
number_2=int(input('введите любое число: '))
print('ваше число - ',number_2)
print('ваша строка - ',string_2)

print('************ Задание 2 ***********')
time=int(input('введите время в секундах: '))
hour=time//3600
minute=time%3600//60
second=time%3600%60
print(hour,minute,second,sep=':')

print('************ Задание 3 ***********')
n=int(input('Введите число: '))
sum=n+n*11+n*111 #можно сразу заменить на 123*n
print('сумма заданных чисел= ',sum)

print('************ Задание 4 ***********')
number_max=int(input('Введите число: '))
max=number_max%10
while number_max%10>0:
    if number_max%10>max:
        max=number_max%10
    number_max=number_max//10
print('Максимальеая цифра числа-',max)

print('************ Задание 5-6 ***********')
profit=int(input('Введите выручку: '))
cost=int(input('Введите издержки: '))
if profit>cost:
    print('Работа была в прибыль на: ',profit-cost)
    employee_number=int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника- ',(profit-cost)/employee_number)
else:
    print('Работа в убыток')

print('************ Задание 7 ***********')
distance_start=int(input('Введите начальный уровень спортсмена: '))
distance_end=int(input('Введите желаемый результат: '))
day=1
while distance_start<distance_end:
    distance_start=distance_start*1.1
    day=day+1
print('Результат достигнут через- ',day)