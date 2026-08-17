"""
Student Command Center - OOP Practice Project
A task management system for students to add, view, complete, and delete tasks.
Demonstrates: Classes, Encapsulation, Properties, Composition, and List Management.
"""
class Student:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def display(self):
        return f"Name: {self.name}\n Branch: {self.branch}\n current Year of Study: {self.year}"


class Task:
    def __init__(self, title, description, deadline, status):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, setStatus):
        if setStatus == "not complete" or setStatus == "completed":
            self.__status = setStatus
        else:
            raise ValueError

    def iscomplete(self):
        return self.__status == "completed"

    def mark_completed(self):
        self.__status = "completed"

    def display(self):
        return f"Title: {self.title}\n Description: {self.description}\n Deadline: {self.deadline}\n Status: {self.__status}"


class StudentCommandCenter:
    def __init__(self, student_object):
        self.task_list = []
        self.student_instance = student_object

    def add_task(self, task):
        self.task_list.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.task_list, start=1):
            print(f"Task {i}")
            print(task.display(), "\n")

    def task_complete(self):
        while True:
            try:
                number = int(input("Enter Task Number to Mark Complete or 0 to Exit: "))
                if number != 0:
                    if self.task_list[number - 1].iscomplete():
                        print("Task Has Already Completed")
                    else:
                        self.task_list[number - 1].mark_completed()
                        print("Task Marked Completed :)")
                else:
                    break
            except IndexError:
                print(f"Task Number {number} Not Found, Try Again")
            except ValueError:
                print("You Enter Invalid Input, Please Enter Valid Number and try again.")

    def delete_task(self):
        while True:
            if not self.task_list:
                break
            try:
                number = int(input("Enter Task Number to Delete Task or 0 to Exit: "))
                if number != 0:
                    self.task_list.pop(number - 1)
                    print("Task Deleted :(")
                    self.view_tasks()
                else:
                    break
            except IndexError:
                print("Task number not found. Please try again.")
            except ValueError:
                print("You Enter Invalid Input, Please Enter Valid Number and try again.")


if __name__ == "__main__":
    prasheek = Student("Prasheek", "Data Science", 3)

    task1 = Task(
        "watch OOP oneshot",
        "watch OOP oneshot so we can apply and work on our project",
        "2026-08-15",
        "completed"
    )

    task2 = Task(
        "watch Flask oneshot",
        "watch OOP oneshot so we can apply and implement Flask into this project",
        "2026-08-20",
        "not completed"
    )

    test1 = StudentCommandCenter(prasheek)
    print(test1.student_instance.name)

    test1.add_task(task1)
    test1.add_task(task2)

    test1.view_tasks()
    test1.task_complete()
    test1.view_tasks()
    test1.delete_task()
    test1.view_tasks()