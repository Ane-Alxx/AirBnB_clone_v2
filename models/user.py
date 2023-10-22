#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
import os

"""
class User(BaseModel):
		email = ''
		password = ''
		first_name = ''
		last_name = ''
"""

class User(BaseModel, Base):
		"""This class defines a user by various attributes"""
		__tablename__ = 'users'
		
		email = Column(
				String(128), nullable=False
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		password = Column(
				String(128), nullable=False
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		first_name = Column(
				String(128), nullable=True
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		last_name = Column(
				String(128), nullable=True
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		places = relationship(
				'Place',
				cascade="all, delete, delete-orphan",
				backref='user'
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
		reviews = relationship(
				'Review',
				cascade="all, delete, delete-orphan",
				backref='user'
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
