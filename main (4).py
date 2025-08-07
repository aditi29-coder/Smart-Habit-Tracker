def habit_tracker():
    print("Welcome to the Smart Habit Tracker!")
    score = 0

    sleep_hours = int(input("How many hours did you sleep today? "))
    if sleep_hours >= 7:
        print("Sleep: Well done! You got enough rest.")
        score += 1
    elif 5 <= sleep_hours < 7:
        print("Sleep: Not bad, but aim for 7–8 hours.")
    else:
        print("Sleep: You need more rest.")

    exercise = input("Did you exercise today? (yes/no): ").lower()
    if exercise == "yes":
        print("Exercise: Good job staying active!")
        score += 1
    else:
        print("Exercise: Try to include at least a short walk.")

    water = input("Did you drink at least 2 liters of water? (yes/no): ").lower()
    if water == "yes":
        print("Water Intake: You’re staying hydrated!")
        score += 1
    else:
        print("Water Intake: Try to drink more water today.")

    screen_time = input("Did you spend more than 2 hours on screen? (yes/no): ").lower()
    if screen_time == "yes":
        print("Screen Time: Try to reduce your screen time.")
    else:
        print("Screen Time: Good job!")
        score += 1

    print(f"\nHealth Score: {score}/4")

    if score == 4:
        print("Excellent! You had a perfect habit day!")
    elif 2 <= score < 4:
        print("You're doing okay, but you can improve.")
    else:
        print("Let’s focus on improving your habits tomorrow.")

    print("\nThanks for using Smart Habit Tracker! Keep growing!")


habit_tracker()
