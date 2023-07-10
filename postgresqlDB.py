from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select, update, delete

engine = create_engine('postgresql://interns:interns%40123@192.168.0.220:5432/interns2',)
meta = MetaData()
