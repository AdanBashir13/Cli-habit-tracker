# lib/helpers.py

from models.user import User
from models.habit import Habit
from models.habit_completion import HabitCompletion

def exit_program():
    print("Goodbye!")
    exit()

def list_users():
    users = User.get_all()
    for user in users:
        print(user)

def create_user():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    try:
        user = User.create(username, password)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating user: ", exc)

def update_user():
    id_ = input("Enter the user id: ")
    if user := User.find_by_id(id_):
        try:
            username = input("Enter the new username: ")
            user.username = username
            password = input("Enter the new password: ")
            user.password = password
            user.update()
            print(f'Success: {user}')
        except Exception as exc:
            print("Error updating user: ", exc)
    else:
        print(f'User {id_} not found')

def delete_user():
    id_ = input("Enter the user id: ")
    if user := User.find_by_id(id_):
        user.delete()
        print(f'Successfully deleted {user}')
    else:
        print(f'User {id_} not found')

def list_habits():
    habits = Habit.get_all()
    for habit in habits:
        print(habit)

def create_habit():
    name = input("Enter the habit name: ")
    frequency = input("Enter the frequency: ")
    user_id = input("Enter the user id: ")
    try:
        habit = Habit.create(name, frequency, user_id)
        print(f'Success: {habit}')
    except Exception as exc:
        print("Error creating habit: ", exc)

def update_habit():
    id_ = input("Enter the habit id: ")
    if habit := Habit.find_by_id(id_):
        try:
            name = input("Enter the new name: ")
            habit.name = name
            frequency = input("Enter the new frequency: ")
            habit.frequency = frequency
            user_id = input("Enter the new user id: ")
            habit.user_id = user_id
            habit.update()
            print(f'Success: {habit}')
        except Exception as exc:
            print("Error updating habit: ", exc)
    else:
        print(f'Habit {id_} not found')

def delete_habit():
    id_ = input("Enter the habit id: ")
    if habit := Habit.find_by_id(id_):
        habit.delete()
        print(f'Successfully deleted {habit}')
    else:
        print(f'Habit {id_} not found')

def list_habit_completions():
    completions = HabitCompletion.get_all()
    for completion in completions:
        print(completion)

def create_habit_completion():
    habit_id = input("Enter the habit id: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        completion = HabitCompletion.create(habit_id, date)
        print(f'Success: {completion}')
    except Exception as exc:
        print("Error creating habit completion: ", exc)

def update_habit_completion():
    id_ = input("Enter the habit completion id: ")
    if completion := HabitCompletion.find_by_id(id_):
        try:
            habit_id = input("Enter the new habit id: ")
            date = input("Enter the new date (YYYY-MM-DD): ")
            completion.habit_id = habit_id
            completion.date = date
            completion.update()
            print(f'Success: {completion}')
        except Exception as exc:
            print("Error updating habit completion: ", exc)
    else:
        print(f'Habit completion {id_} not found')

def delete_habit_completion():
    id_ = input("Enter the habit completion id: ")
    if completion := HabitCompletion.find_by_id(id_):
        completion.delete()
        print(f'Successfully deleted {completion}')
    else:
        print(f'Habit completion {id_} not found')
