# -*- coding: utf-8 -*-

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from nap_todos.views import TodosApi

engine = create_engine('sqlite:///:memory:', echo=False)
db_session = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
api = TodosApi()
app.register_blueprint(api)
