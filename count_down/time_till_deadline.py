from datetime import datetime


def cal_deadline():
    try:
        deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
        today = datetime.today()
        # calculate how many days from now till deadline
        calculation_deadline = deadline_date - today
        hours_till = int(calculation_deadline.total_seconds() / 60 / 60)
        print(f"Dear user the time remaining for your goal:  {goal} is {hours_till} hours")
    except ValueError:
        print("invalid goal or timeframe")


user_input = input("Enter your goal and the date of the deadline separated by a ':' \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
cal_deadline()
