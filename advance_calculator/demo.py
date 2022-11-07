def add():
    return (f"The addition of {num1} and {num2} is "
            f"equal to {num1 + num2}")


"""def subtraction(num1, num2):
    print(num1 - num2)"""

user_input = input("Please enter two number let me add it for you: \n ")
my_add = user_input.split()
num_dict = {"num1": my_add[0], "num2": my_add[1]}
num1 = int(num_dict["num1"])
num2 = int(num_dict["num2"])
cal_num = add()
# print(num_dict)
print(cal_num)
