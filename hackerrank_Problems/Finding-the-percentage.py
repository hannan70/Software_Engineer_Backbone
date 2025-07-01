n = int(input())
student_marks = {}
sum = 0.00
for x in range(0, n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
for marks in student_marks[query_name]:
    sum += marks

result = sum / len(student_marks[name])
print("{:.2f}".format(result))

