
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

print(my_cook_book("recipes.txt"))  # Вывожу получившийся словарь с рецептами

print("\n\n")

cook_book = my_cook_book("recipes.txt") #Создю книгу(словарь) с рецептами для теста функции "get_shop_list_by_dishes()"  

def get_shop_list_by_dishes(dishes, person_count):
    """Функция, которая на входе принимает список блюд из cook_book и количество персон
    для кого мы будем готовить и возвращает словарь с названием ингредиентов и их количеством
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


print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Утка по-пекински'], 10))  # Вывожу получившийся словарь. Для примера
# взял два рецепта с одинаковыми ингридиентами "Помидор"(в Омлете и Фахитос), чтобы продемонстрировать работу функции с
# учетом дополнительного усорвия из задания: "Обратите внимание, что ингредиенты могут повторяться". На каждое из этих
# блюд требуетсмя два помидора.

def concatenate_files_by_number_of_lines(*files):
    """Функция, которая на входе принимает текстовые файлы и объединяет в один новый файл по следующим правилам:
    - Содержимое исходных файлов в результирующем файле сортируется по количеству строк в них (то есть первым записывает
    файл с наименьшим количеством строк, а последним - с наибольшим)
    - Содержимое файла предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
    """
    concatenated_text ={}    
    for file in files:
      with open(file, 'rt', encoding='utf-8') as f:
        text = f.readlines()
        number_of_lines = len(text)
        concatenated_text[file] = (f'{number_of_lines}\n{"".join(text)}\n')
    sorted_text ={k: concatenated_text[k] for k in sorted(concatenated_text, key = concatenated_text.get)} 
    for key, value in sorted_text.items():
      with open('concatenate_files.txt', 'a', encoding='utf-8') as f:
        f.writelines(f'{key}\n{value}\n')

concatenate_files_by_number_of_lines('1.txt', '2.txt', '3.txt') # Создаю объединенный файл


