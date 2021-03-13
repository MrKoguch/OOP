import time
test_list = [-2, -1, 2, 3, 5, 5, 5, 5, 10, 15, 15]
d = 6


def binary_search(array, element_search):
    if array[0] == element_search:
        return 0
    elif array[-1] < element_search:
        return "No item in the list"
    indicies = list(range(len(array)))
    while True:
        array_length = len(array)
        if len(array) == 1:
            if element_search == array[0]:
                return indicies[0]
            return "No item in the list"
        elif array[array_length // 2] < element_search:
            indicies = indicies[array_length // 2:]
            array = array[array_length // 2:]
        elif array[array_length // 2 - 1] < element_search < array[array_length // 2]:
            return "No item in the list"
        elif array[array_length // 2 - 1] < element_search == array[array_length // 2]:
            return indicies[array_length // 2]
        else:
            indicies = indicies[:array_length // 2]
            array = array[:array_length // 2]


start_time = time.perf_counter()
print(binary_search(test_list, d))
finish_time = time.perf_counter()
print(finish_time - start_time)


def b_s(a, value):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while low <= high:
        if value == a[0]:
            return 0
        elif value > a[-1]:
            return "No value"
        elif value > a[mid]:
            low = mid + 1
        elif value == a[mid]:
            if value > a[mid - 1]:
                return mid
            high = mid - 1
        elif value < a[mid]:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return "No value"
    else:
        return mid


start_time = time.perf_counter()
print(b_s(test_list, d))
finish_time = time.perf_counter()
print(finish_time - start_time)
