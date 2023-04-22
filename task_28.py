# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

some_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBB"

def RLE(some_str):
    some_list = list(some_str)
    temp_list = []
    fusion_list = []
    result_list = []


    for i in range(len(some_list) - 1):
        if some_list[i + 1] == some_list[i]:
            temp_list.append(some_list[i])
        else:
            temp_list.append(some_list[i])
            fusion_list.append(temp_list)
            temp_list = []
    if temp_list:
        fusion_list.append(temp_list)
    if some_list[-1] == some_list[-2]:
        fusion_list[-1].append(some_list[-1])
    else:
        fusion_list.append([some_list[-1]])

    temp_list = []

    for i in range(len(fusion_list)):
        temp_list.append()



    return result_list


result_list = RLE(some_str)

a = result_list[0].count('A')
print(a)