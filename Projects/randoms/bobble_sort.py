def bubble_sort(arr): # Define Function
  for i in range(len(arr)): # Iteration on array length
    swapped = False # First swapped = false cause its not swapping
    for x in range(0, len(arr) - i - 1): # Iterating from 0 to last ordered array
      if arr[x] > arr[x + 1]: # If array current index is more than a element current index then it swapps
        swapped = True # Swapped = True cause its more than a last element
        arr[x], arr[x + 1] = arr[x + 1], arr[x] # Swapping the elements right to left
    if not swapped: # If not swapped
      break # Break cause its areadly sorted
  return arr # Returned sorted array 

a = [1, 6, 7, 8, 5, 9, 4, 10, 2] # Unsorted array
print(bubble_sort(a)) # Calls function


