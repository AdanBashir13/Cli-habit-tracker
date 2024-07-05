import sqlite3

CONN = sqlite3.connect('habit_tracker.db')
CURSOR = CONN.cursor()
