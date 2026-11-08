def calculate_bowling_scores(score1, score2, score3, handicap):
    average_score = (score1 + score2 + score3) / 3
    average_with_handicap = average_score + handicap
    return average_score, average_with_handicap


last_name = input("Enter bowler's last name: ")
score1 = float(input("Enter game 1 score: "))
score2 = float(input("Enter game 2 score: "))
score3 = float(input("Enter game 3 score: "))
handicap = float(input("Enter handicap: "))

average_score, average_with_handicap = calculate_bowling_scores(
    score1, score2, score3, handicap
)

print("Bowler:", last_name)
print("Average score:", format(average_score, ".2f"))
print("Average score with handicap:", format(average_with_handicap, ".2f"))
