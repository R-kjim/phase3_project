from config import session,engine
from sqlalchemy import Column,Integer,Boolean,DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime


Base=declarative_base()
class Score(Base):
    __tablename__="scores"

    id=Column(Integer(),primary_key=True)
    student_id=Column(Integer(),nullable=False)
    lesson_id=Column(Integer(),nullable=False)
    quiz_id=Column(Integer(),nullable=False)
    is_correct=Column(Boolean(),nullable=False)
    taken_on=Column(DateTime,default=datetime.now())

    def __init__(self,student_id,lesson_id,quiz_id,is_correct):
        self.student_id=student_id
        self.lesson_id=lesson_id
        self.quiz_id=quiz_id
        self.is_correct=is_correct
        self.taken_on=datetime.now()

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

#method to add a quiz results to the database
def add_score(student_id,lesson_id,quiz_id,is_correct):
    score=Score(student_id,lesson_id,quiz_id,is_correct)
    session.add(score)
    session.commit()



#method that returns a percentage score of a lesson's quiz taken by a student
def lesson_score(lesson_id,student_id):
    scores=session.query(Score).filter_by(lesson_id=lesson_id,student_id=student_id).all()
    correct=0
    if len(scores)==0:
        return f"{0}%"
    else:
        for score in scores:
            if score.is_correct==1:
                correct=correct+1
        ratio=(correct/len(scores))*100
        return f"{ratio}%"
        