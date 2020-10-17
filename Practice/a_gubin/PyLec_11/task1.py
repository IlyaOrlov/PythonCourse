import sqlite3
import json


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def select(self, what=["*"], sources=None, where={}):
        select_part = self.form_select_part(what)
        from_part = self.form_from_part(sources)
        where_part = self.form_where_part(where)
        query = select_part + from_part + where_part
        params = self.form_params(where)
        # print(query)
        # print(params)
        self.cur.execute(query, params)
        row_result = self.cur.fetchall()
        # print(result)
        result = []
        for index in range(len(row_result)):
            obj = {}
            columns_names = self._columns_names(what)
            for key, value in zip(columns_names, row_result[index]):
                obj[key] = value
            result.append(obj)
        return json.dumps(result)

    def form_select_part(self, what):
        return f"SELECT {', '.join(what)} "

    def form_from_part(self, sources):
        if not isinstance(sources, list):
            sources = [sources]
        return f"FROM {', '.join(sources)} "

    def form_where_part(self, where):
        return ("WHERE " + " AND ".join(f"{key}=?" for key in where)) if where else ""

    def form_params(self, where):
        return tuple(where.values()) if where else tuple()

    def _columns_names(self, what):
        return what if what != ['*'] else [tup[0] for tup in self.cur.description]

    def execute(self, query, params):
        self.cur.execute(query, params)
        return json.dumps(self.cur.fetchall())

    def commit(self):
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        return False


if __name__ == '__main__':
    db = DataBase("sqlite.db")
    print(db.select(what=["id", "name"], sources="users", where={"age": 25}))
    print(db.select(what=["id", "name"], sources="users", where={"age": 25, "name": "two"}))
    print(db.select(sources="users"))
    with db:
        db.execute("DELETE FROM users WHERE id=4", ())
        db.execute("INSERT INTO users (id, name, age) VALUES (4, 'four', 25)", ())
    print(db.select(what=["id", "name"], sources="users", where={"age": 25}))
