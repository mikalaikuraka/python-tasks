# Напишите программу, которая считает общую цену.
# Вводится M рублей и N копеек цена, а также
# количество S товара Посчитайте общую цену в 
# рублях и копейках за L товаров. 


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
