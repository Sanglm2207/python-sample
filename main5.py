a = int(input())
b = int(input())
c = int(input())

if len({a, b, c}) == 1:
    print('Equilateral triangle')
elif len({a, b, c}) == 2:
    print('Isosceles triangle')
else:
    print('Scalene triangle')