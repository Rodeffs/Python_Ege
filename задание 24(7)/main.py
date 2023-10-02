"""
Текстовый файл 24-164.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита (ABC…Z). Текст разбит на строки различной длины. Необходимо найти строку, содержащую самую длинную цепочку стоящих подряд одинаковых букв. Если таких строк несколько, надо взять ту, которая в файле встретилась раньше. Определите, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая стоит раньше в алфавите. Запишите в ответе эту букву, а затем – сколько раз она встречается во всем файле.
"""


def chain(s: str) -> int:  # Самая длинная цепочка из одинаковых символов в строке
    letter = s[0]
    count = 1
    max_count = 1
    for i in range(1, len(s)):
        if letter == s[i]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            letter = s[i]
            count = 1
    return max_count


def find_string(text: list):  # Находим строку с самой длинной цепочкой
    max_len = 0
    string_index = 0
    for i in range(len(text)):
        chain_length = chain(text[i])
        if max_len < chain_length:
            string_index = i
            max_len = chain_length
    return text[string_index]


def common_letter(text: list) -> str:  # Находим самый часто встречающийся символ в строке
    string = find_string(text)
    max_count = 0
    max_letter = ""
    for letter in string:
        count = string.count(letter)
        if max_count < count:
            max_count = count
            max_letter = letter
        elif max_count == count and max_letter > letter:
            max_letter = letter
    return max_letter


with open("24-164.txt") as f:
    content = f.read().split()

most_common_letter = common_letter(content)
total_count = "".join(content).count(most_common_letter)  # Преобразуем текст в одну строчку и находим ответ

print(most_common_letter, total_count)
