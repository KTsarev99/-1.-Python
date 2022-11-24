print('введите X координаты 1й точки')
a1 = int (input())
print('введите Y координаты 1й точки')
a2 = int (input())
print('введите X координаты 2й точки')
b1 = int (input())
print('введите Y координаты 2й точки')
b2 = int (input())

x = a1 - b1
y = a2 - b2

len = float ((x*x) + (y*y))
print (len** 0.5)
