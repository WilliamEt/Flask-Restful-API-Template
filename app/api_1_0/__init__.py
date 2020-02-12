from flask import Blueprint

api_1_0 = Blueprint("api_1_0", __name__)

from .views import api_user
