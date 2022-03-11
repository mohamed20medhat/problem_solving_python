def getAvrage(obj, target):
    targeted_person_marks = obj[target]
    person_marks = 0
    for mark in targeted_person_marks :
        person_marks += mark
    avrage_marks = person_marks / len(targeted_person_marks)
    return avrage_marks
    
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(float(getAvrage(student_marks, query_name)))
    print("{:.2f}".format(getAvrage(student_marks, query_name), 2))
    
    
