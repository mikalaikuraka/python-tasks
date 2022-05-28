# Напишите программу, которая считает общую цену.
# Вводится rubles рублей и kopecks копеек цена, а также
# количество quantity товара. Посчитайте общую цену в 
# рублях и копейках. 

MAX_AMOUNT_OF_KOPECKS = 99
NUMBER_FOR_DIVISION = 100

def find_price(rubles, kopecks, quantity):
    rubles *= quantity
    kopecks *= quantity
    if kopecks > MAX_AMOUNT_OF_KOPECKS :
        result = str(rubles + (kopecks // NUMBER_FOR_DIVISION)) + " рублей " + str(kopecks % NUMBER_FOR_DIVISION) + " копеек "
        return result 
    else:  
        result = str(rubles) + " рублей " + str(kopecks) + " копеек " 
        return result


print(find_price(3, 11, 5))
