# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import os

DB_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(DB_FOLDER_PATH, 'server.db')

engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)

Base = declarative_base()

