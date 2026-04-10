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
clubs = set()

for record in records:
   club_part = record.split(":")[1]
   club_list = club_part.split(",")
   for club in club_list:
      clubs.add(club)
print(clubs)
