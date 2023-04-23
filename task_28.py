# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

import random

some_str = "ABBBCCXYZDDDDEEEFFFAAAAAABBBC"
# some_str = ""
# some_str = ''.join([chr(random.randint(65, 70)) for _ in range(10 ** 2)])

def validity(some_str):
        return all(letter.isalpha() for letter in some_str)
def RLE(some_str):
    some_list = list(some_str)
    temp_list, fusion_list, result_list = [], [], []
    if validity(some_str) and len(some_str) != 0:
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
        for i in fusion_list:
            if len(i) > 1:
                result_list.append(i[0])
                result_list.append(i.count(i[0]))
            else:
                result_list.append(i[0])
        result_str = "".join(map(str, result_list))
    else:
        result_str = "Введенная строка невалидна"

    return result_str

print(some_str)
print(RLE(some_str))