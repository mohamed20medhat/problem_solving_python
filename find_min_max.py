# explaination : https://www.youtube.com/watch?v=GVbL4oJlT1s&t=231s

l = [1, 2, 3, 4, 5, 6, 7, 1, 3, 4, 8, 1]

def find_smallest(arr):
    min = 1000000000000000000000
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min


def find_max(arr):
    max = -1000000000000000000000000000000
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max


print(find_max(l))
