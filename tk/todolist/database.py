import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cur = self.conn.cursor()

    def get_tasks(self):
        try:
            sql = "SELECT task, clicks FROM tasks"
            result = {row[0]: int(row[1]) for row in self.cur.execute(sql)}
            if result == None: result = {}
            return result
        except sqlite3.OperationalError:
            self.cur.execute("CREATE TABLE tasks (task text, clicks real)")
            self.get_tasks()

    def add_task(self, task):
        sql = f"INSERT INTO tasks VALUES ('{task}', 0)"
        self.cur.execute(sql)
        self.conn.commit()

    def del_task(self, task):
        sql = f"DELETE FROM tasks WHERE task='{task}'"
        self.cur.execute(sql)
        self.conn.commit()

    def plus_one(self, task):
        sql = f"UPDATE tasks SET clicks=clicks+1 WHERE task = '{task}'"
        self.cur.execute(sql)
        self.conn.commit()

    def minus_one(self, task):
        sql = f"UPDATE tasks SET clicks=clicks-1 WHERE task = '{task}'"
        self.cur.execute(sql)
        self.conn.commit()
