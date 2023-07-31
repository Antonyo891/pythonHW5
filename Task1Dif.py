'''Задача 1 необязательная. Напишите рекурсивную программу вычисления арифметического
выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
*Пример:* 
2+2 => 4; 
1+2*3 => 7; 
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;
Тут может помочь библиотека re'''
import os,random,re
os.system('cls')
def EnterExpression (expression:str=str())->str:
    os.system('cls')
    print("Вводите арифметическое выражение. Используйте операции +,-,/,*. для окончания ввода нажмите = и Enter")
    input1:str=input(expression)
    if input1[len(input1)-1]=='=':
        print ('Конечное выражение:')
        print (expression+input1[1:])
        return expression+input1[1:]
    return EnterExpression(expression+input1)
def CalculatingExpression(expression:str,arithmeticOperations:list=list())->list:
    number:str=''
    for i in expression:
        if i in range(0,10):
            number=number+i
        elif i in ['+','-']:

             
    if re.Match(r'(',expression)!=None:






#expression:str=EnterExpression()
