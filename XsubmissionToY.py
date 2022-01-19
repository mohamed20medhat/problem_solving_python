#hello this is a test 
# it's a problem that i made by myself that i want to write code for. 
#take number X . and onther number Y . and add the number X with Y numbers comming after it. 
# so if we say. 88. and 8 numbers after it. we mean. 88+89+90+91+92+93+94+95. this is a simple calculation for a machine
# but i want to do the algorithm that i thought of. that made me solve it. 

# the algorithm is . multibly X*Y. and then take the small decimals and add them together cause this is an easier calculation. and then add the result of the multiblication to the result of the addition of the smaller numbers




def potato(x,y):
    # x is the main number || Y is the range
    units = (x % 10)
    # now we need to get the smaller dicimal numbers from x. 
    product_result = (x-units) * y
    # i don't want units to move 
    # i will need a container for the original units that gets modified. 
    # then i will need another container for the number that follows it
    original_number = units
    added_to_original = 0

    for i in range(1,y):
        added_to_original = original_number + i
        units += added_to_original  

    submission_result = product_result + units 

    return submission_result


print(potato(88,8))
#print(88+89+90+91+92+93+94+95)
        
