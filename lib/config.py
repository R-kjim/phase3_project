from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = 'sqlite:///course_project.db' 

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()
