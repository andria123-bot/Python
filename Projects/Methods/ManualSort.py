# def manual_sort(arr):
#   n = len(arr)
#   for i in range(n):
#     min_index = i
#     for j in range(i + 1, n):
#       if arr[j] < arr[min_index]:
#         min_index = j
#   arr[i], arr[min_index] = arr[min_index], arr[i]
#   return arr

# numbers = [5, 3, 8, 4, 2, 6]
# print(manual_sort(numbers))

# def manual_counter(lst):
#     count_dict = {}
#     for item in lst:
#         if item in count_dict:
#             count_dict[item] += 1
#         else:
#             count_dict[item] = 1
#     return count_dict

# # Example usage
# items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counts = manual_counter(items)
# print("Item counts:", counts)


name = "Andria"

print(name[::-1])