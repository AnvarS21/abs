import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('postgresql://anvar:1@localhost/orm_db') 
