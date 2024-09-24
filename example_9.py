def main(data: list[int]):
    data = list(map(int, data))
    result_dict = {}
    result_set = []
    sorted_data = sorted(data)

    for index, item in enumerate(sorted_data):
        if item not in result_dict:
            result_dict[item] = index

    result_set = [str(result_dict[item]) for item in data]
    return ' '.join(result_set)

if __name__ == '__main__':
    with open('input.txt', 'r') as file_input:
        data = file_input.readline().split()

print(main(data))
