# Посчитать количество строчных (маленьких) 
# и прописных (больших) букв в введенной строке. 
# Учитывать только английские буквы.

def upper_lower_count(string):
    lower_count = 0
    upper_count = 0
    i = 0
    count = len(string)
    while count:
        if string[i].isalpha():
            if string[i].islower():
                lower_count += 1
            else:
                upper_count += 1
        i += 1
        count -= 1

    print("строчные", lower_count)
    print("прописные", upper_count)

upper_lower_count("HeLlO wOrLd!")