def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.

    if len(list_set_1) > len(list_set_2):
        max_set = list_set_1
        min_set = list_set_2
    else:
        max_set = list_set_2
        min_set = list_set_1
        
    count = 0
    for item in min_set:
        if item in max_set:
            count += 1
    if count == len(max_set):
        return 'Наборы равны.'
    if count == len(min_set):
        return f'Набор {max_set} - супермножество.'
    else:
        return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
