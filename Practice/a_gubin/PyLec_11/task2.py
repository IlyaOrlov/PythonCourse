import sqlite3
import json


class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cur = None
        self.tables = {}

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.tables = {key: self._get_columns_names(key) for key in self._get_existing_tables()}

    def load_data(self, conf_file_name, data_file_name, update_data=False):
        with open(conf_file_name) as file:
            tables_conf = json.load(file)
        self._create_tables(tables_conf)
        if update_data:
            with open(data_file_name) as file:
                tables_data = json.load(file)
            self._fill_tables(tables_data)

    def _create_tables(self, tables_conf):
        for table_conf in tables_conf:
            if table_conf['table_name'] not in self.tables:
                query = [f"CREATE TABLE IF NOT EXISTS {table_conf['table_name']} ( "]
                for column in table_conf['columns']:
                    query.append(f"{column['name']} {column['type']} {column['constraints']}, ")
                query[-1] = query[-1].rstrip(", ")
                query.append(" )")
                self._execute_query(query="".join(query))
                self.tables[table_conf['table_name']] = [column['name'] for column in table_conf['columns']]

    def _fill_tables(self, tables_data):
        for table_data in tables_data:
            table_name = table_data['table_name']
            if table_name in self.tables:
                self._execute_query(query=f"DELETE FROM {table_name}")
                query = [f"INSERT INTO {table_name} ({', '.join(self.tables[table_name])}) VALUES "]
                params = []
                for row in table_data['values']:
                    query.append(f"({', '.join('?' * len(row))}), ")
                    params += row
                query[-1] = query[-1].rstrip(", ")
                self._execute_query(query="".join(query), params=tuple(params))

    def _execute_query(self, query, params=(), get_result=False):
        self.cur.execute(query, params)
        self.conn.commit()
        if get_result:
            return self.cur.fetchall()

    def _get_existing_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name not like 'sqlite_%'")
        tables = self.cur.fetchall()
        return [tup[0] for tup in tables]

    def _get_columns_names(self, table_name):
        self.cur.execute(f"PRAGMA table_info({table_name})")
        row_result = self.cur.fetchall()
        columns_names = [row_data[1] for row_data in row_result]
        return columns_names

    def query_1(self):
        row_result = self._execute_query("SELECT producers.name "
                                         "FROM producers, goods "
                                         "WHERE producers.id == goods.producer_id AND price <= 10 "
                                         "GROUP BY producer_id "
                                         "HAVING count(producer_id) >= 2", get_result=True)
        print(f"Shops with cheep goods: {[tup[0] for tup in row_result]}")

    def query_2(self):
        row_result = self._execute_query("SELECT DISTINCT producers.name, customers.name "
                                         "FROM producers, customers, orders, goods "
                                         "WHERE producers.id == goods.producer_id and "
                                         "      goods.id == orders.goods_id and "
                                         "      customers.id == orders.customer_id "
                                         "ORDER BY producers.name", get_result=True)
        result = {}
        for key, value in row_result:
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]
        print(f"Shop's customers: {result}")

    def query_3(self):
        row_result = self._execute_query("SELECT producers.name, goods.name, max(cg) "
                                         "FROM (SELECT goods_id AS gid, count(goods_id) AS cg "
                                         "      FROM orders "
                                         "      GROUP BY goods_id), "
                                         "      producers, "
                                         "      goods "
                                         "WHERE producers.id == goods.producer_id and "
                                         "      goods.id == gid "
                                         "GROUP BY producers.name", get_result=True)
        print(f"Shop's popular goods: {row_result}")

    def query_4(self):
        row_result = self._execute_query("SELECT pn, gn, gp * count(orders.id) "
                                         "FROM (SELECT producers.name AS pn, "
                                         "             goods.name AS gn, "
                                         "             goods.id AS gid, "
                                         "             goods.price AS gp "
                                         "      FROM producers, goods "
                                         "      WHERE producers.id == goods.producer_id) "
                                         "      LEFT JOIN orders ON gid == orders.goods_id "
                                         "GROUP BY gn "
                                         "ORDER BY pn", get_result=True)
        result = {}
        for goods_stat in row_result:
            producer, goods, proceeds = goods_stat
            if producer in result:
                result[producer][goods] = proceeds
            else:
                result[producer] = {goods: proceeds}
        print(f"Shop's proceeds: {result}")


if __name__ == '__main__':
    db = DB("task2.db")
    db.connect()
    db.load_data("tables_conf.json", "tables_data.json", update_data=True)
    db.query_1()
    db.query_2()
    db.query_3()
    db.query_4()
