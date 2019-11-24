from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, ForeignKeyConstraint
from dao.orm.entities import *

Base = declarative_base()
class Dish(Base):
    __tablename__ = 'dish'
    dishname = Column(String(80), primary_key = True)
    calories_amount = Column(Integer, nullable=False)

class Type(Base):
    __tablename__ = "type"
    typename = Column(String(80), primary_key= True)

class Receipt(Base):
    __tablename__ = 'receipt'
    dishname_fk = Column(Integer, ForeignKey('dish.dishname'), primary_key=True)
    receipt_content = Column (String(100), primary_key = True)
    def __init__(self, receipt_content, dishname_fk):
        self.dishname_fk = dishname_fk
        self.receipt_content = receipt_content
class Ingridients(Base):
    __tablename__ = 'ingridient'

    ingridientname = Column(String(80), primary_key = True)
    def __init__(self, ingridientname):
        self.ingridientname = ingridientname


class Dish_Type(Base):
    __tablename__ = 'dish_type'
    dishname = Column(String(255), ForeignKey('Dish.dishname'), primary_key=True)
    type = Column(String(255), primary_key=True)

