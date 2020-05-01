# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
# Импортируем os для проверки существования файла базы данных
import os


def configure_db(conn):
    cur = conn.cursor()

    # Создаем таблицу Employees
    cur.execute("CREATE TABLE Employees"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Position  CHAR(64)   NOT NULL,"
                "     Bonus     INTEGER    DEFAULT 0,"
                "     Login     CHAR(16)   NOT NULL,"
                "     Password  CHAR(16)   NOT NULL)")

    # Создаем таблицу Projects
    cur.execute("CREATE TABLE Projects"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL)")

    # Создаем таблицу PositionSalary
    cur.execute("CREATE TABLE PositionSalary"
                "    (Position  CHAR(64)   PRIMARY KEY  NOT NULL,"
                "     Salary    INTEGER    NOT NULL)")

    # Создаем таблицу EmployeeProject
    cur.execute("CREATE TABLE EmployeeProject"
                "    (EmployeeId  INTEGER,"
                "     ProjectId   INTEGER,"
                "     PRIMARY KEY (EmployeeId, ProjectId))")

# Добавление записей в таблицу Проект
def insert_project(conn, name):
    # Создаем курсор - специальный объект,
    # который делает запросы и получает их результаты
    cur = conn.cursor()
    # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("INSERT INTO Projects (Name)"
                " VALUES (:name)",
                {'name': name})
    # Если мы не просто читаем, но и вносим изменения в базу данных
    # - необходимо сохранить транзакцию
    conn.commit()

# Добавление записей в таблицу ДолжностьОклад
def insert_position(conn, position, salary):
    cur = conn.cursor()
    cur.execute("INSERT INTO PositionSalary (Position, Salary)"
                " VALUES (:position, :salary)",
                {'position': position, 'salary': salary})
    conn.commit()

# Добавление записей в таблицу Сотрудник
def insert_employee(conn, name, position, bonus, login, pwd):
    cur = conn.cursor()
    cur.execute("INSERT INTO Employees (Name, Position, Bonus, Login, Password)"
                " VALUES (:name, :position, :bonus, :login, :pwd)",
                {'name': name, 'position': position, 'bonus': bonus,
                 'login': login, 'pwd': pwd})
    conn.commit()

# Добавление записей в таблицу СотрудникПроект
def add_employee_to_project(conn, employee_id, project_id):
    cur = conn.cursor()
    cur.execute("INSERT INTO EmployeeProject (EmployeeId, ProjectId)"
                " VALUES (:employeeId, :projectId)",
                {'employeeId': employee_id, 'projectId': project_id})
    conn.commit()

# Проверка наличия пользователя в базе данных
# с указанным логином/пролем
def authentication(conn, login, pwd):
    cur = conn.cursor()
    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("SELECT E.Id, E.Name, E.Position, EP.ProjectId"
                " FROM Employees AS E, EmployeeProject AS EP"
                " WHERE E.Id = EP.EmployeeId"
                " AND E.Login = :login AND E.Password = :pwd",
                {'login': login, 'pwd': pwd})
    # Получаем результат сделанного запроса
    return cur.fetchone()

def authentication2(conn, login, pwd):
    cur = conn.cursor()
    cur.execute("SELECT E.Id, E.Name, E.Position, EP.ProjectId"
                " FROM Employees AS E, EmployeeProject AS EP"
                " WHERE E.Id = EP.EmployeeId"
                " AND E.Login = ? AND E.Password = ?",
                (login, pwd))
    return cur.fetchone()

def bad_authentication(conn, login, pwd):
    cur = conn.cursor()
    cur.execute("SELECT E.Id, E.Name, E.Position, EP.ProjectId"
                " FROM Employees AS E, EmployeeProject AS EP"
                " WHERE E.Id = EP.EmployeeId"
                " AND E.Login = '{login}' AND E.Password = '{pwd}'".
                format(login=login, pwd=pwd))
    return cur.fetchone()


# Вывод информации для менеджера проекта
# Соединяем таблицы Employees, PositionSalary, EmployeeProject
def show_manager_info(conn, project_id):
    cur = conn.cursor()
    cur.execute("SELECT E.Id, E.Name, P.Salary + E.Bonus As Pay"
                " FROM Employees AS E, PositionSalary AS P, "
                "      EmployeeProject AS EP"
                " WHERE E.Position = P.Position"
                " AND E.Id = EP.EmployeeId"
                " AND EP.ProjectId = :project_id",
                {'project_id': project_id})
    print("Информация для менеджера:")
    for row in cur.fetchall():
        print(dict(row))

# Вывод информации для сотрудника
# Соединяем таблицы Employees, PositionSalary
def show_employee_info(conn, employee_id):
    cur = conn.cursor()
    cur.execute("SELECT E.Id, E.Name, P.Salary + E.Bonus As Pay"
                " FROM Employees AS E, PositionSalary AS P"
                " WHERE E.Position = P.Position"
                " AND E.Id = :employee_id",
                {'employee_id': employee_id})
    print("Информация для сотрудника:")
    for row in cur.fetchall():
        print(dict(row))

# Проверка наличия указанного сотрудника в указанном проекте
def is_employee_in_project(conn, employee_id, project_id):
    cur = conn.cursor()
    cur.execute("SELECT EP.ProjectId"
                " FROM EmployeeProject AS EP"
                " WHERE EP.EmployeeId = :employee_id"
                " AND EP.ProjectId = :project_id",
                {'employee_id': employee_id, 'project_id': project_id})
    return bool(cur.fetchone())

# Изменение премии сотрудника
def update_employee_bonus(conn, employee_id, new_bonus):
    cur = conn.cursor()
    # Делаем UPDATE запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("UPDATE Employees"
                " SET Bonus = :new_bonus"
                " WHERE Id = :employee_id",
                {'employee_id': employee_id, 'new_bonus': new_bonus})
    conn.commit()

# Удаление сотрудника из проекта (но не из базы данных)
def delete_employee_from_project(conn, employee_id, project_id):
    cur = conn.cursor()
    # Делаем DELETE запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("DELETE FROM EmployeeProject"
                " WHERE EmployeeId = :employee_id"
                " AND ProjectId = :project_id",
                {'employee_id': employee_id, 'project_id': project_id})
    conn.commit()


def drop_db(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE Employees")
    cur.execute("DROP TABLE Projects")
    cur.execute("DROP TABLE PositionSalary")
    cur.execute("DROP TABLE EmployeeProject")


if __name__ == "__main__":
    db_name = "ogo.db"
    db_exists = os.path.exists(db_name)

    # Подключаемся к базе данных
    # Если файл базы данных еще не создан, он создастся автоматически.
    # Если указать :memory: вместо имени файла - база будет создана
    # в оперативной памяти без сохранения в файле.
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    if not db_exists:
        configure_db(conn)

        insert_project(conn, "Важный")
        insert_project(conn, "Срочный")
        insert_position(conn, "инженер", 50000)
        insert_position(conn, "старший инженер", 51000)
        insert_position(conn, "менеджер проекта", 100000)
        insert_employee(conn, "Иванов И.И.", "инженер", 30000,
                        "ivanovi", "ivanov123")
        insert_employee(conn, "Петров П.П.", "старший инженер", 50000,
                        "petrovp", "p1e2t3")
        insert_employee(conn, "Сидоров С.С.", "менеджер проекта", 30000,
                        "sidorovs", "zayka88")
        add_employee_to_project(conn, 1, 1)
        add_employee_to_project(conn, 2, 1)
        add_employee_to_project(conn, 2, 2)
        add_employee_to_project(conn, 3, 2)

    login = input("Логин: ")
    pwd = input("Пароль: ")
    res = bad_authentication(conn, login, pwd)
    if res:
        user = dict(res)
        print("Здравствуйте, {}".format(user['Name']))
        if user['Position'] == "менеджер проекта":
            show_manager_info(conn, user['ProjectId'])

            id_upd = int(input("Изменение премии. ID сотрудника (0 - отмена): "))
            if id_upd:
                if (id_upd != user['Id'] and
                        is_employee_in_project(conn, id_upd, user['ProjectId'])):
                    new_bonus = input("Новая премия: ")
                    update_employee_bonus(conn, id_upd, new_bonus)
                else:
                    print("Невозможно изменить премию для данного сотрудника")

            id_del = int(input("Удаление сотрудника. ID сотрудника (0 - отмена): "))
            if id_del:
                if id_del != user['Id']:
                    delete_employee_from_project(conn, id_del, user['ProjectId'])
                else:
                    print("Невозможно удалить данного сотрудника из проекта")
        else:
            show_employee_info(conn, user['Id'])
    else:
        print("Доступ запрещен")

    # Не забываем закрыть соединение с базой данных после работы
    conn.close()
