from Scripts.core.handlers.table_handler import registering, display_table, updating, deleting
from fastapi import APIRouter
from schemas.models import to_delete, to_register, to_update
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

app = APIRouter()

engine = create_engine('postgresql://interns:interns%40123@192.168.0.220:5432/internsb2')
meta = MetaData()
a_table = Table(
    "AKHILA1", meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('course', String),
)
meta.create_all(engine)


@app.post("/student_registration")
def func1(data: to_register):
    try:
        return registering(data, engine, a_table)
    except Exception as e:
        print("errorr:", str(e))


@app.get("/to_read_data")
def func2():
    try:
      return display_table(engine, a_table)
    except Exception as e:
        print("errorr:", str(e))



@app.post("/to_update")
def func3(data: to_update):
    try:
      return updating(data, engine, a_table)
    except Exception as e:
        print("errorr:", str(e))


@app.delete("/to_delete")
def func4(data: to_delete):
    try:
       return deleting(data, engine, a_table)
    except Exception as e:
        print("errorr:", str(e))
