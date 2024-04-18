#!/usr/bin/python3
""" SQL storage engine for HBNB project """
import os
from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DB storage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(os.getenv('HBNB_MYSQL_USER'),
                   os.getenv('HBNB_MYSQL_PWD'),
                   os.getenv('HBNB_MYSQL_HOST'),
                   os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        objs = {}
        if cls is not None and cls in classes:
            query = self.__session.query(classes[cls])
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs.update({key: obj.to_dict()})
        else:
            for cls in classes.values():
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs.update({key: obj.to_dict()})
        return objs

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.remove()
