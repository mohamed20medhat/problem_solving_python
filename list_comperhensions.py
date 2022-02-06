# the first solution. where i didn't use list comperhensions 

l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i + j + k != n):
                l.append([i,j,k])
print(l)

# the second solution using list comperhensions 
l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k!=n) ]
print(l)

