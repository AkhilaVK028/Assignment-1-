
from sqlalchemy import select,update,delete


def registering(data,engine,a_table):
    try:
        insert_statement = a_table.insert().values(name=data.name, course=data.course)
        with engine.begin() as connection:
            connection.execute(insert_statement)
        print("successfully registered")
        return "successfully registered "
    except Exception as e:
        print("error")
        print(str(e))
        return "error"


def display_table(engine,a_table):
    try:
        with engine.connect() as connection:
            select_statement = select(a_table)  # selecting
            result = connection.execute(select_statement)  # executing
            rows = result.fetchall()  # fetching
            list = []
            for row in rows:
                id, name, lastname = row
                print(f"ID: {id}, Name: {name}, Lastname: {lastname}")
                list.append([f"ID: {id}, Name: {name}, Lastname: {lastname}"])
            return list
    except Exception as e:
        print("error")
        print(str(e))
        return "error"


def updating(data,engine,a_table):
    try:
        update_statement = (
            update(a_table)
            .where(a_table.c.id == data.id)
            .values(name=data.names, course=data.courses)
        )
        with engine.begin() as connection:
            connection.execute(update_statement)

        return f"row is updated"

    except Exception as e:
        print("error")
    print(str(e))
    return "error"


def deleting(data,engine,a_table):
    try:

        delete_statement = delete(a_table).where(a_table.c.id == data.id)

        with engine.begin() as connection:
            connection.execute(delete_statement)

        return "row is deleted successfully"

    except Exception as e:
        print("error")
        print(str(e))
        return "error"
