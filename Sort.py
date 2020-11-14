import random
import time

def is_sorted(before: list, after: list) -> bool:

    if sorted(before) == after:
        return True
    else:
        print(f'BEFORE: {before}')
        print(f'AFTER : {after}')
        return False

def quick_sort(a: list) -> list:
    if len(a) <= 1:
        return a
    
    left = []
    right = []

    for i in range(1, len(a)):
        if a[i] <= a[0]:
            left.append(a[i])
        else:
            right.append(a[i])
    
    sorted_list = quick_sort(left)
    sorted_list.append(a[0])
    right_sorted = quick_sort(right)
    sorted_list.extend(right_sorted)
    return sorted_list

def selection_sort(a: list) -> list:
    unsorted_list = a.copy()
    sorted_list = []

    while len(unsorted_list) > 0:
        min_index = 0
        for i in range(1, len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[min_index]:
                min_index = i
        sorted_list.append(unsorted_list[min_index])
        unsorted_list.pop(min_index)
    
    return sorted_list


def main():
    print('Let\'s sorting!')

    sorting_algo = [
        quick_sort
        ,selection_sort
    ]

    test_lists = [
        random.sample(range(1,1000), 200)
        #,[]
        #,[0]
    ]

    for algo in sorting_algo:
        for unsorted_list in test_lists:
            start_time = time.time()
            sorted_list = algo(unsorted_list)
            print(f'{algo.__name__} Cost:{time.time() - start_time:.6f} Result:{is_sorted(unsorted_list, sorted_list)}')

if __name__ == '__main__':
    main()