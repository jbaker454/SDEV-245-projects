items = ["a", 20, 30, 40, 50]


def sum_array(arr):
    total = 0


    for i in range(len(arr)):
        if type(i) != type(int):
            return None
        total += arr[i]
    return total


result = sum_array(items)
if result == None:
    print("some of the elements in the array were not numbers")
else:
  print("Sum of numbers in the array:", result)
