# Напишите программу, которая считает общую цену.
# Вводится rubles рублей и kopecks копеек цена, а также
# количество quantity товара. Посчитайте общую цену в 
# рублях и копейках. 


def find_price(rubles, kopecks, quantity):
    rubles *= quantity
    kopecks *= quantity
    if kopecks > 99 :
        result = str(rubles + (kopecks // 100)) + " рублей " + str(kopecks % 100) + " копеек "
        return result 
    else:  
        result = str(rubles) + " рублей " + str(kopecks) + " копеек " 
        return result


print(find_price(3, 11, 5))
