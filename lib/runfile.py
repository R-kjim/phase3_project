from rich.console import Console # type: ignore
from rich.prompt import Prompt # type: ignore
from user import *
from courses import *
from lessons import *
from enrollment import enroll,student_enrollments
from quiz import add_quiz,all_lesson_quiz
from scores import *
console = Console()

def start_page():
    console.print("\nWelcome to Online Course Program")
    console.print("Select an option below to proceed")
    console.print("1. Login")
    console.print("2. Register")
    choice=Prompt.ask("Enter your choice")
    if choice=='1':
        login_fn()
    if choice=="2":
        prompt_user_details()

def prompt_user_details():
    """Prompt the user for details and add a new user."""

    name = Prompt.ask("Enter user name")
    email = Prompt.ask("Enter user email")
    password = Prompt.ask("Enter user password", password=True)
    # role=Prompt.ask("Enter your role")

    # Validate user input
    if not name or not email or not password:
        raise ValueError("All fields are required")

    # Create user (replace with your actual user creation logic)
    user = create_user(name, email, password)
    console.print(f"User created{user}", style="bold green")

def login_fn():
    email=Prompt.ask("Enter your email")
    password=Prompt.ask("Enter your password", password=True)
    value=login(email)
    if value.password==password and value.role=="Admin":
        admin_menu(value)
    if value.password==password and value.role=="Instructor":
        instructor_menu(value)
    if value.password==password and value.role=="Student":
        student_menu(value)

def admin_menu(value):
    print(f"\nWelcome {value.name}. Select an option below to proceed.\n"
          "1. Add an instructor\n2. Add a student\n3. Logout")
    choice=Prompt.ask("Select an option")
    if choice=="1":
        name = Prompt.ask("Enter user name")
        email = Prompt.ask("Enter user email")
        password = Prompt.ask("Enter user password", password=True)
        create_user(name,email,password,"Instructor")
        admin_menu(value)
    if choice=="2":
        name = Prompt.ask("Enter user name")
        email = Prompt.ask("Enter user email")
        password = Prompt.ask("Enter user password", password=True)
        student=create_user(name,email,password,"Student")
        print(f"Select a course from below to enroll {student.name}")
        print(list_courses())
        input=Prompt.ask("Select")
        course=course_instance(int(input))
        enroll(student.id,course.id)
        admin_menu(value)
    if choice=="3":
        start_page()

def instructor_menu(value):
    print(f"\nHello {value.name}? Welcome to your instructor's menu. Select an option below to proceed.\n"
          "1. View my courses\n2. Add a new course\n3. Logout")
    choice=Prompt.ask("Select")
    if choice=="1":
        print(instructor_courses(value.id)["table"])
        print("Select a course id to add/delete/update course lessons.\nEnter 0 to exit. ")
        choice1=Prompt.ask("Select")
        if choice1=="0":
            instructor_menu(value)
        else:
            if int(choice1) in instructor_courses(value.id)["id"]:
                course_menu(int(choice1))
            else:
                print("Invalid course choice")
                instructor_menu(value)
    if choice=="2":
        title=Prompt.ask("Enter course title")
        category=Prompt.ask("Enter course category")
        create_course(title,value.id,category)
        instructor_menu(value)
    if choice=="3":
        start_page()

def course_menu(course_id):
    course=course_instance(course_id)
    print(f"\nAdd or change details about {course.title} here. Select an appropriate choice below")
    print("1. Add a lesson\n2. Update lesson details\n3. Add a quiz\n4. Delete a lesson\n5. Logout ")
    choice=Prompt.ask("Select")
    if choice=="1":
        title=Prompt.ask("Enter lesson title")
        content=Prompt.ask("Enter lesson content")
        add_lesson(title,course_id,content)
        print(f"Lesson titled {title} was added successfully to the {course.title} course.")
        course_menu(course_id)
    if choice=="2":
        print("Select a lesson id from the table below to edit details of a lesson")
        print(all_course_lessons(int(course_id))["table"])
        lesson_id=Prompt.ask("Enter lesson id")
        lesson=lesson_instance(int(lesson_id))["lesson"]
        title=Prompt.ask("Press Enter to keep lesson title unchanged",default=lesson.title)
        content=Prompt.ask("Press Enter to keep lesson content unchanged",default=lesson.content)
        update_lesson(lesson_id,title,content,lesson.lesson_number)
        course_menu(course_id)
    if choice=="3":
        print("Select a lesson")
        print(all_course_lessons1(course_id)["table"])
        lesson_id1=Prompt.ask("Enter")
        if int(lesson_id1) not in [lesson.id for lesson in all_course_lessons1(course_id)["lessons"]]:
            print("Enter a valid lesson")
            lesson_id1=Prompt.ask("Enter")
        question=Prompt.ask("Enter question")
        option1=Prompt.ask("Enter first choice")
        option2=Prompt.ask("Enter second choice")
        option3=Prompt.ask("Enter third choice")
        print("Enter 1,2 or 3 to enter the correct answer from the above choices")
        choice3=Prompt.ask("Select")
        if choice3=="1":
            correct_ans=option1 
        elif choice3=="2":
            correct_ans=option2
        elif choice3=="3":
            correct_ans=option3
        add_quiz(lesson_id1,question,option1,option2,option3,correct_ans)
        course_menu(course_id)
    if choice=="4":
        print("Select a lesson id from the table below to delete the lesson")
        all_course_lessons(course_id)["table"]
        choice2=Prompt.ask("Select")
        delete_lesson(int(choice2))
        course_menu(course_id)
    if choice=="5":
        start_page()

def student_menu(value):
    print(f"Welcome {value.name} to your student profile.")
    if student_enrollments(value.id):
        print("Here are the courses you are enrolled to.\n"
          "Enter the course id to proceed and view course content.")
        print(student_enrollments(value.id)["table"])
        choice=Prompt.ask("Select")
        if int(choice) in student_enrollments(value.id)["course_ids"]:
            print(all_course_lessons(int(choice),value.id)["table"])
            choice2=Prompt.ask("Select a lesson to view its contents")
            print(lesson_instance(int(choice2))["table1"])
            
            print("TAke quiz?\n1. Yes\n2. No\n3. Logout")
            choice3=Prompt.ask("Select")
            if choice3=="1":
                score=0
                for quiz in all_lesson_quiz(int(choice2)):
                    
                    print(f"{quiz.id}. {quiz.question}\n"
                        f"A. {quiz.option1}\nB. {quiz.option2}\nC. {quiz.option3}")
                    ans=Prompt.ask("Enter your answer")
                    ans1=ans.upper()
                    if ans1=="A":
                        correct=quiz.option1
                    if ans1=="B":
                        correct=quiz.option2
                    if ans1=="C":
                        correct=quiz.option3
                    if correct==quiz.correct_ans:
                        score=score+1
                        is_correct=True
                    else:
                        is_correct=False
                    add_score(value.id,int(choice2),quiz.id,is_correct)
                console.print(f"You scored {lesson_score(int(choice2),value.id)}")
                print("1. Back to start page\n2. Logout")
                option=Prompt.ask("Select")
                if option=="1":
                    student_menu(value)
                if option=="2":
                    start_page()
            if choice3=="2":
                student_menu(value)
            if choice3=="3":
                start_page()
        else:
            print("Invalid choice")
            student_menu(value)
    else:
        print("You are currently not enrolled to any course.")
        choice=Prompt.ask("Select")

start_page()

# print(all_course_lessons(int("1"))["table"])