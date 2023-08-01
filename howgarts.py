# # students = ["Hermione", "Harry", "Ron", "Draco"]
# # houses = ["Gryffindor", "Gryffindor","Gryffindor","Slytherin"]
# # print(students)

# # for student in students:
# #     print(student)

# # for i in range(len(students)):
# #     print(i,students[i])

# #dictionaries

# students = {"Hermione": "Gryffindor", "Harry": "Gryffindor",
#             "Ron": "Gryffindor", "Draco": "Slytherin"}

# # print(students["Hermione"])
# # print(students["Harry"])
# # print(students["Ron"])
# # print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=" is ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"],student["house"], student["patronus"], sep=" - ")
