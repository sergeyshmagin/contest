from array import array as ar


def valid_mountain_array(data: ar):
    switch = True
    peak = max(data)

    if len(data) <= 3 or data[0] == peak or data[-1] == peak:
        return False
    else:
        for i in range(len(data)):
            if data[i+1] <= data[i]:
                peak = data.index(data[i])
                break
        for i in range(peak, len(data)-1):
            if data[i+1] >= data[i]:
                switch = False
                break

    return switch


with open('input.txt', 'r') as file_input:
    mountain_data = ar('b', list(map(int, file_input.readline().split())))

print(valid_mountain_array(mountain_data))
