from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import Users, Questions, Responses, RecText, Recommendations
