def cal_per_day(num_of_days, conversion_unit):
    if conversion_unit == "hours" or "hrs":
        return f"{num_of_days} days are {num_of_days * 24} Hours"
    elif conversion_unit == "minutes" or "min":
        return f"{num_of_days} days are {num_of_days * 24 * 60} Minutes "
    elif conversion_unit == "second" or "sec":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} Second"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_number = int(days_and_unit_dict["days"])
        # conversion only for positive value
        if user_input_number > 0:
            my_var = cal_per_day(user_input_number, days_and_unit_dict["unit"])
            print(my_var)
        # conversion only for zero value
        elif user_input_number == 0:
            print("This is a 0 value, please input a positive value")
        # conversion only for negative value if it is not a positive value or zero
        else:
            print("You entered a negative number pls enter a positive number ")
    # the below condition is executed if none of the above function is executable
    except ValueError:
        print("Your input is not a valid number /positive value")
