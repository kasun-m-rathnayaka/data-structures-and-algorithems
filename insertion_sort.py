arr = [23,12,34,56,23,45,13,1]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] =key
        print(arr)

insertion_sort(arr)
