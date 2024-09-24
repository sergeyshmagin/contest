def is_correct_bracket_seq(seq: list):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in seq:
        if char in bracket_pairs.values():  # If it's a left bracket
            stack.append(char)
        elif char in bracket_pairs.keys():  # If it's a right bracket
            if not stack or stack.pop() != bracket_pairs[char]:  # Check for matching
                return False

    return not stack  # Return True if stack is empty, meaning all brackets matched

# Reading from input file   
with open('input.txt', 'r') as file_input:
    seq_1 = file_input.readline().strip()  # Remove any extra whitespace/newlines
    seq = list(seq_1)  # Convert the string to a list of characters

print(is_correct_bracket_seq(seq))