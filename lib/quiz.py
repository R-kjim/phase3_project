from sqlalchemy import Column, Integer, String, ForeignKey, DateTime  # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime
from config import engine, session
from rich.prompt import Prompt # type: ignore


Base = declarative_base()

class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer(), primary_key=True)
    lesson_id = Column(Integer())
    question = Column(String()) 
    option1=Column(String(),default=None)
    option2=Column(String(),default=None)
    option3=Column(String(),default=None)
    correct_ans=Column(String(),default=None)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self,lesson_id,question,option1,option2,option3,correct_ans):
        self.lesson_id=lesson_id
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.correct_ans=correct_ans
        self.created_at=datetime.now()

    def __repr__(self):
        return f"<Quiz(question={self.question}, lesson_id={self.lesson_id})>"
# Create the table
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# Method to add a quiz
def add_quiz(lesson_id,question,option1,option2,option3,correct_ans):
    quiz=Quiz(lesson_id,question,option1,option2,option3,correct_ans)
    session.add(quiz)
    session.commit()
    print("Quiz added successfully")

# Method to delete a quiz
def delete_quiz(quiz_id):
    quiz=session.query(Quiz).filter_by(id=quiz_id).one()
    if quiz:
        session.delete(quiz)
        session.commit()
    else:
        print(f"No question exists with ID {quiz_id}")

# Method to update a quiz
def update_quiz(quiz_id, question=None, option1=None,option2=None,option3=None,correct_ans=None):
    quiz=session.query(Quiz).filter_by(id=quiz_id).one()
    if quiz:
        if question:
            quiz.question = question
        if option1:
            quiz.option1 = option1
        if option2:
            quiz.option2=option2
        if option3:
            quiz.option3=option3
        if correct_ans:
            quiz.correct_ans=correct_ans
        session.commit()
    else:
        print(f"No quiz exists with ID {quiz_id}")

#method that returns all quizzes of a particular lesson
def all_lesson_quiz(lesson_id):
    quizzes=session.query(Quiz).filter_by(lesson_id=lesson_id).all()
    return quizzes


