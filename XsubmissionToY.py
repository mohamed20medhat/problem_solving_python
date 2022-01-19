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
    print(units)
    
    for i in range(y):
        units += units+1
    submission_result = product_result + units 
    print(product_result)
    print(units)

    return submission_result


print(potato(88,8))
# print(88+89+90+91+92+93+94+95)
        
