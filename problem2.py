def calculatescores(score1, score2,score3):
    totalpoints = score1 + score2 + score3
    average = totalpoints / 3
    return totalpoints, average

lastname = input("Enter student last name: ")
score1 = float(input("Enter exam 1 score: "))
score2 = float(input("Enter exam 2 score: "))
score3 = float(input("Enter exam 3 score: "))

totalpoints, average = calculatescores(score1, score2, score3)

print("Student last name:", lastname)
print("Total points:", format(totalpoints, ".2f"))
print("Average exams score:", format(average, ".2f"))
