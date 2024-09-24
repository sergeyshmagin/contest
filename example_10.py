def main(data):
    char_index_map = {}
    max_length = 0
    start = 0  # Начало окна

    for end in range(len(data)):
        if data[end] in char_index_map:
            # Если символ уже есть в подстроке, сдвигаем начало окна
            start = max(start, char_index_map[data[end]] + 1)
        
        # Обновляем индекс текущего символа
        char_index_map[data[end]] = end
        
        # Вычисляем длину текущей подстроки
        max_length = max(max_length, end - start + 1)

    return max_length

if __name__ == '__main__':
    with open('input.txt', 'r') as file_import:
        data = list(file_import.readline().strip())  # Убираем пробелы и символы новой строки
    print(main(data))