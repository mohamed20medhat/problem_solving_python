# explaination : https://www.youtube.com/watch?v=GVbL4oJlT1s&t=231s

l = [1, 2, 3, 4, 5, 6, 7, 1, 3, 4, 8, 1]

def find_min(arr):
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


# another way 
# notice that when using for num in nums. num is not an itterator. it's the actual value of the item of the array. not a loop varyable that has auto_increment or auto_decrement 
def min_max_list(arr, min_max):
    if min_max == "min" : 
        min = 100000000000000000
        for i in arr : 
            if min > i: 
                min = i
        return min 
    elif min_max == 'max' : 
        max =  -10000000000000000000000000
        for y in arr : 
            if max < y: 
                max = y
        return max

print (min_max_list(l,'max'))
print (min_max_list(l,'min'))
print(find_max(l))
print(find_min(l))