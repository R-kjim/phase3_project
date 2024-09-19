from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from config import engine, session
from courses import Course  # Import Course for the foreign key reference
from tabulate import tabulate

Base = declarative_base()

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    lesson_number = Column(Integer, unique=True,nullable=False)
    is_available = Column(Boolean, default=True)
    course_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    # Relationship with Course
    # course = relationship('Course', backref='lessons')
    def __init__(self,title,course_id,lesson_number,content,is_available=True):
        self.title=title
        self.course_id=course_id
        self.lesson_number=lesson_number
        self.content=content
        self.is_available=is_available
        self.created_at=datetime.now()
        

    def __repr__(self):
        return f"<Lesson(title={self.title}, course_id={self.course_id}, lesson_number={self.lesson_number})>"

# Create the lessons table
Base.metadata.create_all(engine)

# Method to add a lesson to the database
def add_lesson(title,course_id,lesson_number,content):
    lesson=Lesson(title,course_id,lesson_number,content)
    session.add(lesson)
    session.commit()
    

# Method to update a lesson
def update_lesson(lesson_id, title=None, content=None, lesson_number=None, is_available=None):
    lesson=session.query(Lesson).filter_by(id=lesson_id).one()
    if title:
        lesson.title = title
    if content:
        lesson.content = content
    if lesson_number is not None:
        lesson.lesson_number = lesson_number
    if is_available is not None:
        lesson.is_available = is_available
    print(f"Lesson {lesson_id} details updated successfully.")
    session.commit()

# Method to delete a lesson
def delete_lesson(lesson_id):
    lesson=session.query(Lesson).filter_by(id=lesson_id).one()
    if lesson_id:
        session.delete(lesson)
        session.commit()
        print(f"Lesson {lesson_id} successfully deleted.")
    else:
        print(f"No lesson exists with id {lesson_id}")

def all_course_lessons(course_id):
    """Get all lessons of a course"""
    lessons=session.query(Lesson).filter_by(course_id=course_id).all()
    headers=["Lesson Title","Lesson Number"]
    rows=[[lesson.title,lesson.lesson_number]for lesson in lessons]
    print( tabulate(rows,headers,tablefmt="fancy_grid"))

def lesson_instance(lesson_id):
    return session.query(Lesson).filter_by(id=lesson_id).one()