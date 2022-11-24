print('введите координаты x, y')
x = int(input())
y = int(input())

print(type(x))
print(type(y))


# print('номер четверти плоскости - ')
if (x>0 and y>0) :
    print('1')
elif x<0 and y>0 :
    print('2')
elif x<0 and y<0 :
    print('3')
elif x>0 and y<0  :
    print('4')
else :
    print('X ≠ 0 и Y ≠ 0')

