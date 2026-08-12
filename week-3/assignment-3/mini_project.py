day = input("What day is it? ").strip().lower()
time = input("What time of day? (morning, afternoon, evening) ").strip().lower()

# --- weekday validation ---
valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
valid_times = ["morning", "afternoon", "evening"]

if day not in valid_days:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
elif time not in valid_times:
    print("Sorry, I don't recognize that time of day. Choose: morning, afternoon, evening.")
else:

# --- activity suggestions ---
    if day == "monday":
        if time == "morning":
            suggestion = "Great time for planning your week and setting goals."
        elif time == "afternoon":
            suggestion = "Perfect for tackling your most important task."
        else:
            suggestion = "Relax with a book or movie to unwind."

    elif day == "tuesday":
        if time == "morning":
            suggestion = "Morning study, great time to focus!"
        elif time == "afternoon":
            suggestion = "Good afternoon for project work or study."
        else:
            suggestion = "Nice evening for cooking something new."

    elif day == "wednesday":
        if time == "morning":
            suggestion = "Midweek boost, try a quick workout."
        elif time == "afternoon":
            suggestion = "Great time to review your progress for the week."
        else:
            suggestion = "Perfect evening for a midweek break."

    elif day == "thursday":
        if time == "morning":
            suggestion = "Start early and get ahead on tomorrow’s tasks."
        elif time == "afternoon":
            suggestion = "Good time for collaboration or meetings."
        else:
            suggestion = "Wind down with a favorite show."

    elif day == "friday":
        if time == "morning":
            suggestion = "Finish strong and wrap up your weekly goals."
        elif time == "afternoon":
            suggestion = "Great time to close out tasks before the weekend."
        else:
            suggestion = "Enjoy Friday night with friends or family!"

    elif day == "saturday":
        if time == "morning":
            suggestion = "Perfect morning for errands or a fun outing."
        elif time == "afternoon":
            suggestion = "Great afternoon for hobbies or exploring."
        else:
            suggestion = "Perfect night for a movie or trying a new recipe."

    elif day == "sunday":
        if time == "morning":
            suggestion = "Nice morning for quiet time or reflection."
        elif time == "afternoon":
            suggestion = "Good time to prepare for the week ahead."
        else:
            suggestion = "Relax and recharge before Monday."

    print("Suggestion:", suggestion)
    