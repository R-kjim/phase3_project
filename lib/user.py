from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from sqlalchemy.exc import NoResultFound
from config import engine, session
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Store hashed password in practice
    role=Column(String)
    created_at=Column(String)

    def __init__(self, name, email, password,role="Admin"):
        self.name = name
        self.email = email
        self.password = password  # Hash password in practice
        self.role=role
        self.created_at=datetime.now()

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"

# Create the table
Base.metadata.create_all(engine)

def create_user(name, email, password,role="Admin"):
    """Create a new user."""
    user = User(name=name, email=email, password=password,role=role)
    session.add(user)
    session.commit()
    print(f"User created: {user}")
    return user

# def add_new_user(name, email, password):
#     """Add a new user to the database."""
#     return create_user(name, email, password)

def delete_table():
    """Drop the users table."""
    Base.metadata.drop_all(engine)
    print("Users table deleted.")

def delete_user(user_id):
    """Delete a user by ID."""
    user = session.query(User).filter_by(id=user_id).one()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} deleted.")
    else:
        print(f"No user found with ID {user_id}.")

def update_user(user_id, name=None, email=None, password=None):
    """Update user information."""
    try:
        user = session.query(User).filter_by(id=user_id).one()
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password  # Hash password in practice
        session.commit()
        print(f"User with ID {user_id} updated: {user}")
    except NoResultFound:
        print(f"No user found with ID {user_id}.")

def login(email):
    user=session.query(User).filter_by(email=email).one()
    return user
