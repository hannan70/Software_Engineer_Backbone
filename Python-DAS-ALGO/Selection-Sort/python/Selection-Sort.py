def selection_sort(number, size):

    # outer loop for all numbers
    for i in range(size):
        min_index = i

        # inner loop for find the min index
        for j in range(i+1, size):
            if number[j] < number[min_index]:
                min_index = j

        # swap two numbers
        if min_index != i:
            # first way for swap
            # temp = number[i]
            # number[i] = number[min_index]
            # number[min_index] = temp

            # second way for swap
            (number[i], number[min_index]) = (number[min_index], number[i])


numbers = [3, 44, 38, 1, 27, 2, 4]
size = len(numbers)
selection_sort(numbers, size)
print("After sorting array")
print(numbers)
