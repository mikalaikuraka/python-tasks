#Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника. 
# Если стороны определяют треугольник, найти его площадь. 
# Если нет, вывести сообщение о неверных данных.

SQRT = 0.5

def get_triangle_square(a, b ,c):
    if b + c > a and a + c > b and a + b > c:
        perimetr = (a + b + c) / 2

        return (perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)) ** SQRT
    else:
        return "Неверные данные"


print(get_triangle_square(3,4,5))