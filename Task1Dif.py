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
        print (expression+input1[:len(input1)-1])
        return expression+input1[:len(input1)-1]
    return EnterExpression(expression+input1)
def ExpressionInList(expression:str,list2:list=list())->list:
   string:str=''
   list1:list=list2
   for i in expression:
       if i in [str(items) for items in range(0,10)]:
           string=string+i
           expression=expression[1:]
       elif i=='(':
           if string!='':
               list1.append(string)
               string=''
           end:int=re.search('(\))',expression).end()
           expression1=expression[1:end-1]
           expression=expression[end:]
           list1.append(ExpressionInList(expression1,[]))
           break
       elif i in ['*','+','-','/']:
           if string!='':
               list1.append(string)
               string=''
           list1.append(i)
           expression=expression[1:]
           break
   if string!='':
       list1.append(string)
       string=''
   if len(expression)>0:
       return ExpressionInList(expression,list1)
   else:
       return list1
#def CalculatingExpression(expressioon:list)->int:



string =EnterExpression()
list1=ExpressionInList(string)
print(list1)
