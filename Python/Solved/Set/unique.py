records = [
    "Arun:AI,ML,Robotics",
    "Bala:ML,IoT",
    "Chitra:AI,CyberSecurity",
    "Divya:Robotics,IoT,AI",
    "Ezhil:ML,CyberSecurity",
    "Farah:AI,ML",
    "Ganesh:IoT,Robotics,AI",
    "Hari:ML"
]
students = set()
for record in records:
    name = record.split(":")[0]
    students.add(name)

print(students)
