list=[]
answer_a=0
answer_b=0
#Функция для подсчета суммы цифр
def sum_number(number):
    sum=0
    while number//10!=0:
        sum=sum+number%10
        number=number//10
    sum=sum+number%10
    return(sum)
#Задание А-C
for number in range(1,1001):
    if number%2!=0:
        list.append(number**3)
        if sum_number(number**3)%7==0:
            answer_a=answer_a+sum_number(number**3)
        if sum_number(number**3+17)%7==0:
            answer_b=answer_b+sum_number(number**3+17)

print('ответ задания А: ',answer_a)
print('ответ задания B: ',answer_b)



