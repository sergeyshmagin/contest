# Success Package ID: 118688218

def main(data: list[int], limit: int) -> int:
    """
    Calculates the minimum number of pairs of integers from the input list
    that can be formed such that their sum does not exceed the specified limit.

    Parameters:
    data (list[int]): List of integers to be paired.
    limit (int): The upper limit for the sum of each pair.

    Returns:
    int: The minimum number of pairs needed to accommodate all integers
         in the list that are less than the limit.
    """

    counter: int = 0
    # Filtering and sorting data
    data = sorted(item for item in data if item <= limit)

    # If list is empty, return 0
    if not data:
        return 0

    left_pointer: int = 0
    right_pointer: int = len(data) - 1

    # Main loop for finding pairs

    while left_pointer <= right_pointer:
        if data[left_pointer] + data[right_pointer] <= limit:
            left_pointer += 1
            right_pointer -= 1
        else:
            right_pointer -= 1
        counter += 1
    return counter


if __name__ == '__main__':
    with open('input.txt', 'r') as file_input:
        data: list[int] = [int(item) for item in file_input.readline().split()]
        limit: int = int(file_input.readline())

    result = main(data, limit)

    with open('output.txt', 'w') as file_output:
        file_output.write(str(result))
