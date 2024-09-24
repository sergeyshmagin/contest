example_array = [6, 5, 3, 1, 8, 7, 2, 4, 12 ]


def bubble_sort(data):
    # Напишите здесь код сортировки.
    last = len(data) - 1
    switch = True
    while switch:
        switch = False
        for firt_item in range(last):
            if data[firt_item] > data[firt_item + 1]:
                data[firt_item], data[firt_item + 1] = (
                    data[firt_item + 1], data[firt_item]
                )

                switch = True
        last -= 1
    return data


print(bubble_sort(example_array))
