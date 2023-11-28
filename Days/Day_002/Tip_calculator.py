print("Welcome to the tip calculator.")
total = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15?\n"))
total_value = total + (total * tip / 100)
total_people = int(input("How many people to split the bill?\n"))

per_person = total_value / total_people
print(f"Eache person should pay: ${round(per_person,2)}")