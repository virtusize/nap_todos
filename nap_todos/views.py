from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import Integer, Unicode

from flask_nap.api import Api, Debug, JsonDecoder
from flask_nap.view import ModelView
from flask_nap.view_filters import CamelizeFilter
from flask_nap.exception_handlers import UnsupportedMethodExceptionHandler, ModelNotFoundExceptionHandler, ModelInvalidExceptionHandler
from sa_nap.controller import SAModelController
from sa_nap.model import SAModelSerializer, SAModel, Field
from nap.model import ModelSerializer, Model, Storage
from nap.validators import FieldValidator, EnsureNotEmpty, EnsureInt, EnsureMinLength
from nap.controller import ModelController

from app import db_session, app, engine


class Tag(Model):

    _validate_with = [
        FieldValidator('id', EnsureNotEmpty, EnsureInt),
        FieldValidator('name', EnsureNotEmpty, Unicode)
    ]


class Tags(Storage):
    private = Tag(id=1, name='private')
    business = Tag(id=2, name='business')


class TodoList(SAModel):

    id = Field(Integer, primary_key=True)
    name = Field(Unicode(255), validate_constraints=True, validate_with=[EnsureMinLength(3), EnsureNotEmpty()])


class Todo(SAModel):

    id = Field(Integer, primary_key=True)
    name = Field(Unicode(255), validate_constraints=True, validate_with=[EnsureMinLength(3), EnsureNotEmpty()])
    todo_list_id = Field(Integer, ForeignKey('todo_lists.id'), nullable=False, validate_constraints=True)
    todo_list = relationship(TodoList, backref='todos')


class TagController(ModelController):
    model = Tag
    model_storage = Tags


class TagView(ModelView):
    controller = TagController
    filter_chain = [CamelizeFilter]
    serializer = ModelSerializer


class TodoController(SAModelController):
    model = Todo
    session_factory = db_session


class TodoView(ModelView):
    controller = TodoController
    filter_chain = [CamelizeFilter]
    serializer = SAModelSerializer


class TodoListController(SAModelController):
    model = TodoList
    session_factory = db_session


class TodoListView(ModelView):
    controller = TodoListController
    filter_chain = [CamelizeFilter]
    serializer = SAModelSerializer


class TodosApi(Api):
    name = 'api'
    prefix = '/api'
    version = 1
    mixins = [
        Debug(print_request=False, print_response=False),
        JsonDecoder
    ]
    views = [
        TagView,
        TodoView,
        TodoListView
    ]
    exception_handlers = [
        UnsupportedMethodExceptionHandler,
        ModelNotFoundExceptionHandler,
        ModelInvalidExceptionHandler
    ]

api = TodosApi()
app.register_blueprint(api)
SAModel.metadata.create_all(engine)