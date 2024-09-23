# Success Package ID: 118605638

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

    result: int = 0
    counter: int = 0
    # Filtering and sorting data
    data = sorted(item for item in data if item <= limit)

    # If list is empty, return 0
    if not data:
        return 0

    # Remove the element equal to the limit if it exists
    if data[-1] == limit:
        data.pop()  # Remove the last element
        counter += 1

    left_pointer: int = 0
    right_pointer: int = len(data) - 1

    # Main loop for finding pairs
    while left_pointer < right_pointer:
        result = data[left_pointer] + data[right_pointer]

        if result > limit:
            counter += 1  # Count the right element
            right_pointer -= 1  # Move the right pointer
        else:
            counter += 1  # Count the pair
            left_pointer += 1  # Move the left pointer
            right_pointer -= 1  # Move the right pointer

    # If one element remains
    if left_pointer == right_pointer:
        counter += 1  # Account for it

    return counter


with open('input.txt', 'r') as file_input:
    data: list[int] = list(map(int, file_input.readline().split()))
    limit: int = int(file_input.readline())

if __name__ == '__main__':
    result = main(data, limit)

with open('output.txt', 'w') as file_output:
    file_output.write(str(result))
