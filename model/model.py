"""
    This is where the app models are created.
"""

from sqlalchemy import (Column, ForeignKey, Integer, String, Table, Unicode,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///model/db/app.db", echo=True)
Base = declarative_base(engine)

"""
    Class to turn tables into one Python object
"""


class ItemObj(object):

    def __init__(self, item, category):
        super(ItemObj, self).__init__()
        self.id = item.id
        self.name = item.name
        self.category = category


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    sub_name = Column(String(80), nullable=False)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


class User(Base):
    __tablename__ = 'user'
    # primary keys are required by SQLAlchemy
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))


Base.metadata.create_all(engine)
