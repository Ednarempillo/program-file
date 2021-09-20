print("This program will compute and print student average score")

prelim = float(input("Enter Score: "))
midterm = float(input("Enter Score: "))
semifinal = float(input("Enter Score: "))
final = float(input("Enter Score: "))

average = (prelim + midterm + semifinal + final)/4

print("Average Grade: {}!".format(average))

if average >=75:
    print("You PASSED.")
    if average >= 99 and average <= 100:
        print("Grade: A")
    elif average >= 90 and average <=98:
        print("Grade: B")
    elif average >= 80 and average <= 89:
        print("Grade: C")
    elif average >= 75 and average <=79:
        print("Grade: D")
elif average <75:
    print("You FAILED.")
    if average >= 72 and average <=74:
        print("Grade: D")
    elif average >=61 and average <=70:
        print("Grade: D")