## crate a class that accept user input and save it in  object
# class is like an object constructor
# all classes have a __init__() function
# __init__() is executed automatically, whenever we create object from this class

class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}. You can contact them at {self.email} ")
