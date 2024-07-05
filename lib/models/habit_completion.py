from models.__init__ import CURSOR, CONN
from models.habit import Habit
from models.user import User

class HabitCompletion:
    all = {}

    def __init__(self, date, habit_id, user_id, id=None):
        self.id = id
        self.date = date
        self.habit_id = habit_id
        self.user_id = user_id

    def __repr__(self):
        return f"<HabitCompletion {self.id}: Date: {self.date}, Habit ID: {self.habit_id}, User ID: {self.user_id}>"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def habit_id(self):
        return self._habit_id

    @habit_id.setter
    def habit_id(self, habit_id):
        if isinstance(habit_id, int) and Habit.find_by_id(habit_id):
            self._habit_id = habit_id
        else:
            raise ValueError("habit_id must reference a habit in the database")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must reference a user in the database")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS habit_completions (
            id INTEGER PRIMARY KEY,
            date TEXT,
            habit_id INTEGER,
            user_id INTEGER,
            FOREIGN KEY (habit_id) REFERENCES habits(id),
            FOREIGN KEY (user_id) REFERENCES users(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS habit_completions;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO habit_completions (date, habit_id, user_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.date, self.habit_id, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        HabitCompletion.all[self.id] = self

    @classmethod
    def create(cls, date, habit_id, user_id):
        habit_completion = cls(date, habit_id, user_id)
        habit_completion.save()
        return habit_completion

    def update(self):
        sql = "UPDATE habit_completions SET date = ?, habit_id = ?, user_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.date, self.habit_id, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM habit_completions WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del HabitCompletion.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        habit_completion = cls.all.get(row[0])
        if habit_completion:
            habit_completion.date = row[1]
            habit_completion.habit_id = row[2]
            habit_completion.user_id = row[3]
        else:
            habit_completion = cls(row[1], row[2], row[3])
            habit_completion.id = row[0]
            cls.all[habit_completion.id] = habit_completion
        return habit_completion

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM habit_completions"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM habit_completions WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_habit_id(cls, habit_id):
        sql = "SELECT * FROM habit_completions WHERE habit_id = ?"
        rows = CURSOR.execute(sql, (habit_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM habit_completions WHERE user_id = ?"
        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_date(cls, date):
        sql = "SELECT * FROM habit_completions WHERE date = ?"
        rows = CURSOR.execute(sql, (date,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def habit(self):
        return Habit.find_by_id(self.habit_id)

    def user(self):
        return User.find_by_id(self.user_id)
