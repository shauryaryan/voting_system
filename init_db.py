from app import db
from models import User, Vote

# Create all the tables in the database
db.create_all()
print("Tables created successfully.")
