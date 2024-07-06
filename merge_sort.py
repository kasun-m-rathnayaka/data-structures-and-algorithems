arr = [23, 12, 34, 56, 23, 45, 13, 1]


# def merge(arr, left, right):
#     left_i = right_i = arr_i = 0
#
#     while left_i < len(left) and right_i < len(right):
#         if left[left_i] < right[right_i]:
#             arr[arr_i] = left[left_i]
#             left_i += 1
#         else:
#             arr[arr_i] = right[right_i]
#             right_i += 1
#         arr_i = + 1
#
#     while left_i < len(left):
#         arr[arr_i] = left[left_i]
#         left_i += 1
#         arr_i = + 1
#
#     while right_i < len(right):
#         arr[arr_i] = right[right_i]
#         right_i += 1
#         arr_i = + 1
#
#
# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     merge_sort(left)
#     merge_sort(right)
#
#     merge(arr, left, right)
#     return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        left_i = right_i = arr_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                arr[arr_i] = left[left_i]
                left_i += 1
            else:
                arr[arr_i] = right[right_i]
                right_i += 1
            arr_i += 1

        while left_i < len(left):
            arr[arr_i] = left[left_i]
            left_i += 1
            arr_i += 1

        while right_i < len(right):
            arr[arr_i] = right[right_i]
            right_i += 1
            arr_i += 1

    return arr

print(merge_sort(arr))
