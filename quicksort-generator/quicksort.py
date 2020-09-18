import sys
import random


ARR_SIZE_MAX = 100000
SORT_MODES = ('sorted', 'reversed', 'random')


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


if __name__ == '__main__':
    # Check that the required arguments are supplied
    if len(sys.argv) < 3:
        print('ERROR: usage: command <sort mode> <array size>')
        exit(1)

    sort_mode, arr_size = sys.argv[1], int(sys.argv[2])
    # Check semantics of the supplied arguments
    err_msg = ''
    if not 0 < arr_size <= ARR_SIZE_MAX:
        err_msg = 'ERROR: the array size is limited to: [1, {}]'.format(ARR_SIZE_MAX)
    elif sort_mode not in SORT_MODES:
        err_msg = 'ERROR: sort mode can only be one of the following values: {}'.format(SORT_MODES)
    if err_msg:
        print(err_msg)
        exit(1)

    # Create the array which is sorted by default
    sort_array = list(range(arr_size))
    # Change the ordering of elements based on the selected sort mode
    if sort_mode == SORT_MODES[1]:
        sort_array = list(reversed(sort_array))
    elif sort_mode == SORT_MODES[2]:
        random.shuffle(sort_array)

    print('Initial array: {}'.format(sort_array))
    quick_sort(sort_array, 0, arr_size - 1)
    print('Resulting array: {}'.format(sort_array))
