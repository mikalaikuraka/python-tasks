# Требуется: найти сумму цифр введенного числа при условии, 
# что оно одно/дву/трех-значное, в противном случае 
# вывести информацию об ошибке данных.

def sum_of_digits():
    sum = 0
    number = int(input("Введите число:"))
    number = abs(number)
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    return sum


print(sum_of_digits())