'''Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''
import os,random
os.system('cls')
def RaiseToPower (number:int,power:int)->int:
    if power==0:
        return 1
    return RaiseToPower(number,power-1)*number



number:int=random.randint(1,25)
power:int=random.randint(1,5)
numberinpower:int =RaiseToPower(number,power)
print(f'Число {number} в степени {power} = {numberinpower}')