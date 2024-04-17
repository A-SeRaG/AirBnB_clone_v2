#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
=======
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import DataTime
from sqlalchemy import String
>>>>>>> 989f4b7dc80c24fcdb3e86ebf256e18399a9ba33
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("place", backref="cities", cascade="delete")

=======
    state_id = Column(String(60), nullable=False, ForegnKey("states.id"))
>>>>>>> 989f4b7dc80c24fcdb3e86ebf256e18399a9ba33
