print("Enter Marks Obtained in 5 Subjects: ")
english = 44
math = 67
bangla = 94
religion = 99
science = 99

tot = english + math + bangla + religion + science
avg = tot / 5

if avg >= 80 and avg <= 100:
	print("Your Grade is A+")
elif avg >= 70 and avg < 79:
	print("Your Grade is A")
elif avg >= 60 and avg < 69:
	print("Your Grade is A-")
elif avg >= 50 and avg < 59:
	print("Your Grade is B")
elif avg >= 40 and avg < 49:
	print("Your Grade is C")
elif avg >= 33 and avg < 39:
	print("Your Grade is D")
else:
	print("Fail!")
