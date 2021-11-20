studentData = []
studentRegisterData = []

# input student records
numberOfStudents = int(input("Enter the number of students to be sorted:"))
print('number of students are', numberOfStudents)
for i in range(0, numberOfStudents):
    print(
        " Enter the 4 digit register number for student eg: 1001")
    registerNumber = int(input())
    while len(str(registerNumber)) != 4:
        registerNumber = int(input('Error ! Please enter 4 digit number \n'))
    print(
        " Enter the class (A/B)")
    classBatch = input()
    print(
        " Enter the food preferences (V/NV)")
    foodPreference = input()
    ele = [registerNumber, classBatch, foodPreference]
    studentData.append(ele)
print(studentData)

# store student records
for student in studentData:
    if not any(d['registerNumber'] == student[0] for d in studentRegisterData):
        studentRegisterData.append(dict({'registerNumber': student[0], 'batch': student[1], 'preference': student[2]}))
print(studentRegisterData)

# sort the student based on criteria
capacity = 3
result = {'BV': [], 'AV': [], 'BNV': [], 'ANV': [], 'NA': []}

for it in studentRegisterData:
    allocatedHostelStudents = result[it['batch'] + it['preference']]
    if len(allocatedHostelStudents) < capacity:
        result[it['batch'] + it['preference']].append(it['registerNumber'])
    else:
        result['NA'].append(it['registerNumber'])

print("result %result", result)
