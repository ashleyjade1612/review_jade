from datetime import datetime

fullname = "Jade Ashley Villanueva"
print(f"{fullname}")

studentid = "211-0738"
print(f"{studentid}")

now = datetime.now()
 
print(f"{now}")

issue = input("Wats yor networking isyu? ")

with open("network_issue.txt", "w") as file:
	file.write(issue)
