from sqlalchemy import Column, Integer, String, DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime
from config import engine, session
from user import User
from tabulate import tabulate # type: ignore

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    instructor_id = Column(Integer(), nullable=False)
    category = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())


    def __init__(self, title, instructor_id, category):
        self.title = title
        self.instructor_id = instructor_id
        self.category = category
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<Course(title={self.title}, instructor_id={self.instructor_id}, category={self.category})>"

# Create the courses table
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# Methods for creating a course
def create_course(title, instructor_id, category):
    """Create a new course."""
    course = Course(title=title, instructor_id=instructor_id, category=category)
    user=session.query(User).filter_by(id=instructor_id).one()
    #Course can only be added by an instructor
    if user.role=="Instructor":
        session.add(course)
        session.commit()
        print(f"Course created: {course}")
        return course
    else:
        print(f"The id {instructor_id} is not a valid instructor id")

#method to update course details
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

#method to delete a course
def delete_course(course_id):
    """Delete a course by ID."""
    course = session.query(Course).filter_by(id=course_id).one_or_none()
    if course:
        session.delete(course)
        session.commit()
        print(f"Course with ID {course_id} deleted.")
    else:
        print(f"No course found with ID {course_id}")

#returns a tabular representation of all courses
def list_courses():
    """List all courses."""
    courses = session.query(Course).all()
    headers=["Course id","Course Title"]
    rows=[[course.id,course.title]for course in courses]
    return tabulate(rows,headers,tablefmt="fancy_grid")

#returns a tabular presentation and courses id for an instructors courses
def instructor_courses(instructor_id):
    """List courses of an individual instructor"""
    courses=session.query(Course).filter_by(instructor_id=instructor_id).all()
    headers=["ID","Course Title","Category"]

    rows=[[course.id,course.title,course.category] for course in courses]
    courses_id=[course.id for course in courses]
    table1 = tabulate(rows, headers=headers, tablefmt="fancy_grid")
    values={
        "table":table1,
        "id":courses_id
    }
    return values

#method that returns a course instance--filters by course id
def course_instance(course_id):
    """Returns the instance of a single course"""
    course=session.query(Course).filter_by(id=course_id).one()
    return course