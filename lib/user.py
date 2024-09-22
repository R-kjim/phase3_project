from sqlalchemy import Column, Integer, String # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import validates # type: ignore
from config import engine, session
from datetime import datetime
from rich.console import Console # type: ignore
console = Console()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String(), nullable=False)  
    role=Column(String())
    created_at=Column(String())

    def __init__(self, name, email, password,role="Admin"):
        self.name = name
        self.email = email
        self.password = password  
        self.role=role
        self.created_at=datetime.now()

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email

    def __repr__(self):
        if self.role=="Admin":
            return f"<User(name={self.name}, email={self.email})>"

# Create the table
Base.metadata.create_all(engine)

#method to create a new user
def create_user(name, email, password,role="Admin"):
    """Create a new user."""
    user = User(name=name, email=email, password=password,role=role)
    session.add(user)
    session.commit()
    console.print(f"{name} has ben registered successfully for the {role} role.", style="bold green")

#method to delete the table
def delete_table():
    """Drop the users table."""
    Base.metadata.drop_all(engine)
    print("Users table deleted.")

#method to delete a user
def delete_user(user_id):
    """Delete a user by ID."""
    user = session.query(User).filter_by(id=user_id).one()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} deleted.")
    else:
        print(f"No user found with ID {user_id}.")

#method to update user details
def update_user(user_id, name=None, email=None, password=None):
    """Update user information."""
    user = session.query(User).filter_by(id=user_id).one()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password  # Hash password in practice
        session.commit()
        print(f"User with ID {user_id} updated: {user}")
    else:
        print(f"No user found with ID {user_id}.")

#method to return a user filtered by email for login purposes
def login(email):
    user=session.query(User).filter_by(email=email).one()
    return user
