# -*- coding: utf-8 -*-
import logging

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=False)
db_session = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
