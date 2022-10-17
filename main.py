# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

def my_cook_book(text_file):
    """Функция возвращает словарь с рецептами из текстового файла со списком рецептов.
    Рецепты в файле должны быть записаны в формате:
    'Название блюда
    Количество ингредиентов в блюде
    Название ингредиента | Количество | Единица измерения
    Название ингредиента | Количество | Единица измерения
    ...'
    """
    keys = ['ingridient_name', 'quantity', 'measure']
    with open(text_file, encoding='utf-8') as text:
        lines = filter(bool, map(str.strip, text))
        cook_book_dict = {n: [{k: v for (k, v) in zip(keys, map(str.strip, next(lines).split(' | ', 2)))}
                              for _ in range(int(next(lines)))] for n in lines}
    return cook_book_dict


assert type(my_cook_book("recipes.txt")) is dict  # Учусь покрывать тестами)))

print(my_cook_book("recipes.txt"))  # Выводим получившийся словарь с рецептами
print("######################################################################################")
cook_book = my_cook_book("recipes.txt")
#
#
def get_shop_list_by_dishes(dishes, person_count):
    """Функция, которая на вход принимает список блюд из cook_book и количество персон
    для кого мы будем готовить и выводит словарь с названием ингредиентов и его количества
    для блюда, с учетом того, что ингредиенты могут повторяться.
    """
    shop_list_by_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingridient_name'] not in shop_list_by_dishes:
                shop_list_by_dishes[ingredient['ingridient_name']] = {'measure': ingredient['measure'], 'quantity': int(
                    ingredient['quantity']) * person_count}
            else:
                shop_list_by_dishes[ingredient['ingridient_name']]['quantity'] += int(
                    ingredient['quantity']) * person_count
    return shop_list_by_dishes


print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Утка по-пекински'], 10))  # Выводим получившийся словарь.

#
# def concatenate_files_by_number_of_lines(text_file_1):
#     """
#     """
#     with open(text_file_1) as f:
#         count = 0
#         for line in f:
#             count += 1
#
#         list_1 = [text_file_1, count, f.readlines()]
#         print(list_1)


# with open('1.txt') as f:
#     for line in f:
#       print(line, end='')

# list = ['2018-01-01', 'yandex', 'cpc', 100]

# dict = list.pop()

# for i in reversed(list):
#   dict = {i: dict}

# print(dict)
# concatenate_files_by_number_of_lines("1.txt")
# mylist = f.read().splitlines()
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1