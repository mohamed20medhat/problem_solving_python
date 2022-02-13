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

#########################################################################################
#########################################################################################
#########################################################################################

# another solution using dictionary => https://youtu.be/_wnf8s0N0Tk
grades = []
# i will get the grades in a list to find the second smallest number using it
grade_to_name = {}
# i will make a dictionary. that i will store key value pears of grade and a list of students who have got that grade

if __name__ == '__main__':
  for _ in range(int(input())):
    name = input()
    score = float(input())
    grades.append(score)
    if score not in grade_to_name:
      # if there is no key "score" in the dic. create a new key
      grade_to_name[score] = [name]
    else:
      # else -> the key "grade" already exists. add the name to the list of              students who got that grade
      grade_to_name[score].append(name)

  # convert the list to set to remove duplicates. then convert it back into a        list and sort it. to get the second smallest grade
  grades = sorted(set(grades))
  second_min = grades[1]  # the second smallest will have index 1
  # sort the list of names that got the second_smallest_grades in the dictionary     and print each name in it
  grade_to_name[second_min].sort()
  for nm in grade_to_name[second_min]:
    print(nm)














