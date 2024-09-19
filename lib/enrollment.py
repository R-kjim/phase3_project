from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from config import session,engine
from user import User  # To reference student_id
from courses import Course  # To reference course_id

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    is_enrolled = Column(Boolean, default=True)
    enrollment_date = Column(DateTime, default=datetime.now())

    def __init__(self,student_id,course_id,is_enrolled=True):
        self.student_id=student_id
        self.course_id=course_id
        self.is_enrolled=is_enrolled
        self.enrollment_date=datetime.now()

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, is_enrolled={self.is_enrolled})>"

Base.metadata.create_all(engine)

# Method to enroll a student
def enroll(student_id,course_id,is_enrolled=True,):
    enrollment1=Enrollment(student_id,course_id,is_enrolled)
    session.add(enrollment1)
    session.commit()
    print(f"Enrollment successful.")

# Method to update enrollment status
def update_enrollment(self, is_enrolled):
    self.is_enrolled = is_enrolled
    session.commit()

# Method to delete enrollment
def delete_enrollment(self):
    session.delete(self)
    session.commit()
