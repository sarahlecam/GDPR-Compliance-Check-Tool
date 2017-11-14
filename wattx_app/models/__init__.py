from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import Enterprise, EnterpriseData, Questions
