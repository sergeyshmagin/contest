def main(a, b):
    result = a + b
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file_input:
        a = int(file_input.readline())
        b = int(file_input.readline())
    with open('output.txt', 'w') as file_output:
        file_output.write(str(main(a, b)))
