#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref=('state'), cascade='all')

    @property
    def cities(self):
        """ Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id """
        city_list = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
