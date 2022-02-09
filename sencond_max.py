# trying to find the max number first 

# sort it as a list then take the largest and the smallest
def first_method(): 
    l = [1,2,3,4,5,6,7,1,3,4,2,1]
    l.sort()
    print(l[0]) # min
    print(l[-1]) # max
    print(l[-2]) # second_ max
    # now how to print the second largest number ? 
    print(min(l))
    print(max(l))

# the problem with it is that i can't get the second largest element cause i don't know if there are repeated elements in it. if an element was repeated then l[-2] will return the same as l[-1]. so there must be another way


# i can convert the list into a set. and remove the maximum number. then get the max. this will give me the second max num. and this is better cause sets doesn't allow repetion. so no need to worry about multible elements with the same value sorted after each other 
#* array to set solution => https://youtu.be/JiEOD_wlU1U
def second_method_SET():
    li = [1,2,3,4,5,6,7,1,3,4,2,1]
    my_set = set (li)
    print(my_set)
    my_set.remove(max(my_set))
    print(my_set)
    print(max(my_set)) 
# this solution is better cause it solved the problem with repetion. but still the algorithm is bad cause i feel like i can't control it or modify it. like. what if i wanted to get the third element. i will need to do a loop that removes as much as nessacary to get the element that i want. something like this 

li = [1,2,3,4,5,6,7,1,3,4,2,1]
def find_the_x_max_or_min(arr, min_max, number_of_element): 
    my_set = set (arr) 
    if min_max == 'min' : 
        for i in range (number_of_element): 
            my_set.remove(min(my_set))
        return min(my_set)
    if min_max == 'max' : 
        for i in range (number_of_element): 
            my_set.remove(max(my_set))
        return max(my_set)
# note that it starts from 0. so if you wanted to get the max. you put the number_of_element = 0
# print(find_the_x_max_or_min(li,'max',0))

# this is so far the best solution that i got to. but it's still not good enough cause the conversion from list to a set may take more time. but in the same time. if i did it manually i don't know if i could write a more efficient code than this so far. so i will search for better solutions 


#* there is another way. which is to use 2 varyables. 1 will work as the max and the other will work as the second max some thing like this : https://www.youtube.com/watch?v=k2J0kOqYTOk
def find_second_max(arr):
    max_num = -10000000000000000000
    second_max = -10000000000000000000
    for i in arr : 
        if max_num < i :
            second_max = max_num
            max_num = i
        elif (i > second_max) and (i < max_num):
            second_max = i
    return second_max

print(find_second_max(li))





