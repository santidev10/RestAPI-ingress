import app
import pytest
from unittest import mock

@mock.patch('flask_restful.reqparse.RequestParser.parse_args', 'flask_restful.reqparse.RequestParser.parse_args')
def test_substract():
    app.substract() 
    #assert sum ==  "7" 
