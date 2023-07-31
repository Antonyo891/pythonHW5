'''Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4'''
import os,random
os.system('cls')
def sum (summand1:int,summand2:int)->int:
    if summand2==0:
        return 1
    return summand1+sum(1,summand2-1)



number1:int=random.randint(1,1000)
number2:int=random.randint(1,100)
sumNumber12:int=sum(number1,number2)
print(f'Сумма чисел {number1} и {number2} = {sumNumber12}')
