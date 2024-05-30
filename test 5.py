#Create

a = 'hello' #Одинарные ковычки
b = "hello" #Двойные ковычки
c = "i 'know' Python" #Комбинированные
d = 'i "know" Python' #Можно и так
e = 'i 'know" Python" #Ошибка

#Привести к str
a = 123 #Целочисленный тип
a = str(a) #Результат 123
str([1,1.1,'a']) #Результат '[1,1.1,'a']
str(True) #'True'
str(None) #'none'

#print

a = 'hello'
print(a)
print('Ivan')

#Index
a = 'hi'
a[0] # 'h'
a[1] # 'i'
a[3] # Error index

#Методы

'\t hi \n'.strip() # привет. удаляет пробелы и ненапечатанные символы слева и справа от текста
'ww hi ww'.strip('w') #Если передать значение то будет пытаться удалить его слева и справа как w
'ww hi ww'.rstrip('w') #Удаляет символы справа
'Hello world '.partition('o') #Разбивает строку по первому вхождению
