# Требуется: найти сумму цифр введенного числа при условии, 
# что оно одно/дву/трех-значное, в противном случае 
# вывести информацию об ошибке данных.


NUMBER_FOR_DIVISION = 10

def sum_of_digits(number):
    if number.isnumeric():
        sum = 0
        number = abs(int(number))

        while number > 0:
            sum += number % NUMBER_FOR_DIVISION
            number //= NUMBER_FOR_DIVISION
        
        return sum
    else:
        return "Неверный формат данных!"


print(sum_of_digits(input("Введите число:")))