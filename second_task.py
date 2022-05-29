# Требуется: найти сумму цифр введенного числа при условии, 
# что оно одно/дву/трех-значное, в противном случае 
# вывести информацию об ошибке данных.


NUMBER_FOR_DIVISION = 10

def sum_of_digits(number):
    sum = 0
    number = abs(number)
    while number > 0:
        sum = sum + number % NUMBER_FOR_DIVISION
        number = number // NUMBER_FOR_DIVISION
    return sum

print(sum_of_digits(123))