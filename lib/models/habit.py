from models.__init__ import CURSOR, CONN
from models.user import User

class Habit:
    all = {}

    def __init__(self, name, frequency, user_id, id=None):
        self.id = id
        self.name = name
        self.frequency = frequency
        self.user_id = user_id

    def __repr__(self):
        return f"<Habit {self.id}: {self.name}, {self.frequency}, User ID: {self.user_id}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        if isinstance(frequency, str) and len(frequency):
            self._frequency = frequency
        else:
            raise ValueError("Frequency must be a non-empty string")

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
            CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            name TEXT,
            frequency TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS habits;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO habits (name, frequency, user_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.name, self.frequency, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        Habit.all[self.id] = self

    @classmethod
    def create(cls, name, frequency, user_id):
        habit = cls(name, frequency, user_id)
        habit.save()
        return habit

    def update(self):
        sql = "UPDATE habits SET name = ?, frequency = ?, user_id = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.frequency, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM habits WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del Habit.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        habit = cls.all.get(row[0])
        if habit:
            habit.name = row[1]
            habit.frequency = row[2]
            habit.user_id = row[3]
        else:
            habit = cls(row[1], row[2], row[3])
            habit.id = row[0]
            cls.all[habit.id] = habit
        return habit

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM habits"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM habits WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM habits WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def user(self):
        return User.find_by_id(self.user_id)
