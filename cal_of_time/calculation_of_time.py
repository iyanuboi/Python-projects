from helper import validate_and_execute

user_input = ""
# the below function is executed for the program to continue
while user_input != "stop":
    user_input = input("Enter number of days and conversion unit \n")
    days_and_unit = user_input.split(": ")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dict)
