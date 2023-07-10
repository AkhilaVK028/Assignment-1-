from Scripts.core.DB.postgresqlDB import meta, engine
from pydantic import BaseModel
from sqlalchemy import Column, Table, String, Integer


class to_register(BaseModel):
    name: str
    course: str


class to_update(BaseModel):
    id: int
    names: str
    courses: str


class to_delete(BaseModel):
    id: int

# try:
#     a_table = Table(
#         "a", meta,
#         Column('id', Integer, primary_key=True),
#         Column('name', String),
#         Column('course', String),
#     )
#     meta.create_all(engine)
# except Exception as e:
#     print("error")
#     print(str(e))