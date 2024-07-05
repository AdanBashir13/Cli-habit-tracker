#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.user import User
from models.habit import Habit
from models.habit_completion import HabitCompletion

def reset_database():
    HabitCompletion.drop_table()
    Habit.drop_table()
    User.drop_table()
    User.create_table()
    Habit.create_table()
    HabitCompletion.create_table()

    # Create seed data
    user1 = User.create("Adan", "12345678")
    user2 = User.create("Bashir", "87654321")

    habit1 = Habit.create("Exercise", "Daily", user1.id)
    habit2 = Habit.create("Read", "Daily", user1.id)
    habit3 = Habit.create("Meditate", "Weekly", user2.id)
    habit4 = Habit.create("Journal", "Daily", user2.id)

    HabitCompletion.create("2023-07-01", habit1.id, user1.id)
    HabitCompletion.create("2023-07-02", habit2.id, user1.id)
    HabitCompletion.create("2023-07-03", habit3.id, user2.id)
    HabitCompletion.create("2023-07-04", habit4.id, user2.id)

reset_database()
print("Database has been reset with seed data")
