def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


while True:
    print("\nSorting Algorithm Menu:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        input_list = list(
            map(int, input("Enter space-separated numbers to sort: ").split()))
        bubble_sort(input_list)
        print("Sorted List (Bubble Sort):", input_list)

    elif choice == '2':
        input_list = list(
            map(int, input("Enter space-separated numbers to sort: ").split()))
        selection_sort(input_list)
        print("Sorted List (Selection Sort):", input_list)

    elif choice == '3':
        input_list = list(
            map(int, input("Enter space-separated numbers to sort: ").split()))
        insertion_sort(input_list)
        print("Sorted List (Insertion Sort):", input_list)

    elif choice == '4':
        print("Exiting the Sorting Algorithm Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")


# map(int, ...) is used to convert the user's input, which is initially a string of space-separated numbers, into a list of integers. This is a common way to convert and process input when you expect the input to be a sequence of values.
