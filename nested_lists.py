# the first solution : https://youtu.be/pGMj6ScxWTY
n_inputs = int(input())
student_data = []
grades = []
for i in range(n_inputs):
    name = input()
    mark = float(input())
    student_data.append([name, mark])
    grades.append(mark)
# i will need to convert the list to a set to be able to sort it without the duplicates
grades = sorted(set(grades))
# sorted method -> converts the set to a sorted array
second_smallest_grade = grades[1] # => the second smallest grade 

# i will need to get the names of the students who has the second_smallest_grade
name = [] 
for stu in student_data:
    # stu is the smaller array that contains each student's data. 0 -> name || 1 -> grade
    if stu[1] == second_smallest_grade:
        name.append(stu[0])

# to get the sorted names of the students who got the second_smallest_grade
name.sort()
for nm in name :
    print(nm)








