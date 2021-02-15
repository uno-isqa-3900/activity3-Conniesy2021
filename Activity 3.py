# "Connie"
# "ISQA 3900 Web Application Development"
# "Data: 30/01/2021"
# "Calculate the grade of achievement"

# Displays the title of the program when called
def display_title():
    print("Welcome to the Grade Calculator")

# This function prompts the user for and reads the total points earned
def get_totalPoints():
    test_score = int(input("Enter the total score (0-1000):"))
    while test_score < 0 or test_score > 1000:
       print("This is an error. You must enter test_score >= 0 and test_score <= 1000. Try again ")
       test_score = int(input("Enter the total score (0-1000):"))
    return test_score
# This functions receives the average grade from the main()
# and returns the letter grade based on the average earned.
def get_letterGrade(averageEarned):
    if 92 <= averageEarned <= 100:
        return "A+"
    elif 88 <= averageEarned <= 92.99:
        return "B+"
    elif 82 <= averageEarned <= 87.99:
        return "B"
    elif 78 <= averageEarned <= 81.99:
        return "C+"
    elif 70 <= averageEarned <= 77.99:
        return "C"
    elif 60 <= averageEarned <= 69.99:
        return "D"
    else:
        return "F"

# The main function
def main():
    display_title()
    total_points = get_totalPoints()
    averageEarned = total_points/1000*100
    letterGrade = get_letterGrade(averageEarned)
    print("You earned an average of",averageEarned,"%",".Letter grade earned:",letterGrade,)
    choice = "y"
    choice = input("Would you like to enter another score (y/n)?")
    while choice.lower() == "y":
        total_points = get_totalPoints()
        averageEarned = total_points / 1000 * 100
        get_letterGrade(averageEarned)
        letterGrade = get_letterGrade(averageEarned)
        print("You earned an average of",averageEarned,"%",".Letter grade earned:",letterGrade,)
        choice = input("Would you like to enter another score (y/n)?")

if __name__ == "__main__":
    main()




