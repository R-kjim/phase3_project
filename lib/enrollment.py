from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime
from config import session,engine
from tabulate import tabulate # type: ignore

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer(), nullable=False)
    course_id = Column(Integer(), nullable=False)
    is_enrolled = Column(Boolean(), default=True)
    enrollment_date = Column(DateTime, default=datetime.now())

    def __init__(self,student_id,course_id,is_enrolled=True):
        self.student_id=student_id
        self.course_id=course_id
        self.is_enrolled=is_enrolled
        self.enrollment_date=datetime.now()

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id}, is_enrolled={self.is_enrolled})>"

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
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

#method that returns course ids and a tabular presentation of courses a student is enrolled to
def student_enrollments(student_id):
    from courses import course_instance
    enrollments=session.query(Enrollment).filter_by(student_id=student_id,is_enrolled=1).all()
    student_courses=[course_instance(enrollment.course_id) for enrollment in enrollments]
    headers=["ID","Course Title","Category"]
    rows=[[course.id,course.title,course.category] for course in student_courses]
    table=tabulate(rows,headers=headers,tablefmt="fancy_grid")
    course_ids=[course.id for course in student_courses]
    if len(rows)==0:
        return None
    else:
        return {"table":table,"course_ids":course_ids}