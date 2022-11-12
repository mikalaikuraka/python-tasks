# Города и страны

# Заданы *N* стран, включающие в себя города. 
# Заданы *Q* запросов. Каждый запрос - название города, 
# на который нужно вывести страну, к которому он относится (если относится).

# Формат ввода:

# В первой строки число *N* - количество стран

# Далее по порядку задаются страны одна за другой, каждая в следующем формате:

# В отдельной строке число *K* - количество городов в стране.

# В следующих *K* строках по одному городу (город может состоять из нескольких слов)

# После ввода городов задаётся *Q* - число запросов.

# В следующих *Q* строках задаются города (их может и не существовать).

# Input

# 3
# United States of America
# 6
# New York
# San Francisco 
# Mayami
# Chicago
# Saint Petersburg
# New Orleans
# Belarus
# 2
# Minsk
# Grodno
# Russia
# 3
# Moscow
# Saint Petersburg
# Smolensk
# 4
# Minsk
# Chicago
# Saint Petersburg
# Smolensk

# Output

# Belarus
# United States of America
# ['Russia', 'United States of America']
# Russia

# Да, может быть и такое, что в двух странах могут 
# находиться разные города с одинаковым названием. 
# Реализация этого функционала - план максимум, на десяточку.

dct = {}
array = []
arr = []
count = 0

number_of_countries = int(input("Введите количество стран:"))

for i in range(number_of_countries):
    country = input("Введите страну:")
    number_of_cities = int(input("Количество городов:"))

    for j in range(number_of_cities):
        arr.append(input("Введите город:"))
        tpl = tuple(arr)
    
    arr.clear()
    dct[tpl] = country

number_to_search = int(input("Введите количество городов для поиска:"))

for el in range(number_to_search):
    city = input("Введите город:")
    for i in dct:
        for j in i:
            if city in j:
                count +=1

    if count > 1:
        array = [dct[i] for i in dct for j in i if city in j]
        print(array)
    else:
        for i in dct:
            for j in i:
                if city in j:
                    print(dct[i])
    
    count = 0
