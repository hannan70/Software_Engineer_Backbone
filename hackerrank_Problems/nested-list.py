n = int(input())
record_list = []
gradeList = []
final = []
for i in range(0, n):
    student_name = input()
    student_grade = float(input())
    # input name and score
    record_list.append([student_name, student_grade])

# convert dict
record_list_ = dict(record_list)

# push only value
for j in record_list_.values():
    gradeList.append(j)

# convert set for unique value
cv_set = set(gradeList)

# convert list for sorting
sortedList = list(cv_set)
sortedList.sort()

# get the second lowest grade
clean_list = sortedList[1]

# check second lowest grade and find name then push
for k in record_list:
    if k[1] == clean_list:
        final.append(k[0])

# print final name
for name in sorted(final):
    print(name)
