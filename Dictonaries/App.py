costumer = {
    "name": "Ahmad Ja'far Ali",
    "age": 22,
    "is_verified": True
}
# costumer["name"] = "Jafar Ali"
# print(costumer.get("birthdate", "May 16 2001"))

costumer["birthdate"] = "May 16 2001"
print(costumer["birthdate"])

# Challenge
phone = input("Phone: ")
diggit_mapping = {
    "1": "Satu",
    "2": "Dua", 
    "3": "Tiga", 
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
}
output = ""
for ch in phone:
    output += diggit_mapping.get(ch, "!") + " "
print(output)