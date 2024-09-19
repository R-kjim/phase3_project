from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from config import engine, session
from user import User
from tabulate import tabulate

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructor_id = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    # # Relationship with User (Instructor)
    # instructor = relationship('User', backref='courses')

    def __init__(self, title, instructor_id, category):
        self.title = title
        self.instructor_id = instructor_id
        self.category = category
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<Course(title={self.title}, instructor_id={self.instructor_id}, category={self.category})>"

# Create the courses table
Base.metadata.create_all(engine)

# Methods for interacting with courses

def create_course(title, instructor_id, category):
    """Create a new course."""
    course = Course(title=title, instructor_id=instructor_id, category=category)
    user=session.query(User).filter_by(id=instructor_id).one()
    if user.role=="Instructor":
        session.add(course)
        session.commit()
        print(f"Course created: {course}")
        return course
    else:
        print(f"The id {instructor_id} is not a valid instructor id")
    
    

def update_course(course_id, title=None, category=None):
    """Update a course's title or category."""
    course = session.query(Course).filter_by(id=course_id).one_or_none()
    if course:
        if title:
            course.title = title
        if category:
            course.category = category
        session.commit()
        print(f"Course updated: {course}")
    else:
        print(f"No course found with ID {course_id}")

def delete_course(course_id):
    """Delete a course by ID."""
    course = session.query(Course).filter_by(id=course_id).one_or_none()
    if course:
        session.delete(course)
        session.commit()
        print(f"Course with ID {course_id} deleted.")
    else:
        print(f"No course found with ID {course_id}")

def list_courses():
    """List all courses."""
    courses = session.query(Course).all()
    headers=["Course id","Course Title"]
    rows=[[course.id,course.title]for course in courses]
    return tabulate(rows,headers,tablefmt="fancy_grid")

def instructor_courses(instructor_id):
    """List courses of an individual instructor"""
    courses=session.query(Course).filter_by(instructor_id=instructor_id).all()
    headers=["ID","Course Title","Category"]

    rows=[[course.id,course.title,course.category] for course in courses]
    table = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    return table
def course_instance(course_id):
    """Returns the instance of a single course"""
    course=session.query(Course).filter_by(id=course_id).one()
    return course