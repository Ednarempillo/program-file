print("This program will compute and print student average score")

prelim = float(input("Enter Score: "))
midterm = float(input("Enter Score: "))
semifinal = float(input("Enter Score: "))
final = float(input("Enter Score: "))

average = (prelim + midterm + semifinal + final)/4
print("Average grade: {}!".format(average))

print("Average grade: ")
if average >=75:
    print("You PASSED.")
elif average <75:
    print("You FAILED.")
