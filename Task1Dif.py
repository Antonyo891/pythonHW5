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
def CalculatingExpression(expression:str,list1:list)->list:
   string:str=None
   if len(expression)==0:
       return list1
   for i in expression:
       if int(i) in range(0,10):
           string=string+i
           expression=expression.replace(i,'')
       elif i=='(':
           list1.append(string)
           string=None
           end:int=re.match(r')',expression).start()
           expression1=expression[:end]
           expression=expression[end:]
           expression=expression+CalculatingExpression(expression1,list1)
       elif i in ['*','+','-','/']:
           list1.append(i)
           expression=expression.replace(i,'')
       else:
            return list1



string =EnterExpression()
list1=CalculatingExpression(string)
