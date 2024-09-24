# length = 10
# data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def main(length, data: list):
    result_set = []
    result_set.extend(data)
    
    for item in data:
        left = 0
        right = length - 1
        
        while left <= right:
            mid = (left + right) // 2
            if item == data[mid]:
                if result_set.count(item) > 1:
                    result_set.remove(item)
                    result_set.append('_')
            if int(item) < int(data[mid]):
                right = mid - 1
            else:
                left = mid + 1
    return result_set


if __name__ == '__main__':
    with open('input.txt', 'r') as file_input:
        length = int(file_input.readline())
        data = file_input.readline().split()
    # print(f'input: {data}')
    str = ' '.join(main(length, data))
    # print(str)
    with open('output.txt', 'w') as file_output:
        file_output.write(str)
