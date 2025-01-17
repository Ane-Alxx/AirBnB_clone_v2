#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.base_model import Base
import os

class City(BaseModel):
		""" The city class, contains state ID and name """

		"""#!/usr/bin/python3
		City Module for HBNB project
			from models.base_model import BaseModel


			class City(BaseModel):
		state_id = 
		name = 
		"""
		__tablename__ = 'cities'
		
		name = Column(
				String(128), nullable=False
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		state_id = Column(
				String(60), ForeignKey('states.id'), nullable=False
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		places = relationship(
				'Place',
				cascade='all, delete, delete-orphan',
				backref='cities'
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
