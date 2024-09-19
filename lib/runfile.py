from rich.console import Console
from rich.prompt import Prompt
from user import create_user,delete_table,delete_user,update_user,login
from courses import create_course,update_course,delete_course,list_courses,instructor_courses,course_instance
from lessons import add_lesson,all_course_lessons,lesson_instance,update_lesson,delete_lesson
from enrollment import enroll

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
    print(f"\nWelcome {value.name}. Select an option below to proceed.\n"
          "1. View my courses\n2. Add a new course\n3. Logout")
    choice=Prompt.ask("Select")
    if choice=="1":
        print(instructor_courses(value.id))
        print("Select a course id to add/delete/update course lessons.\nEnter 0 to exit.) ")
        choice1=Prompt.ask("Select: ")
        if choice1=="0":
            instructor_menu(value)
        else:
            course_menu(int(choice1))
    if choice=="2":
        title=Prompt.ask("Enter course title")
        category=Prompt.ask("Enter course category")
        create_course(title,value.id,category)
    if choice=="3":
        start_page()

def course_menu(course_id):
    course=course_instance(course_id)
    print(f"\nAdd or change details about {course.title} here. Select an appropriate choice below")
    print("1. Add a lesson\n2. Update lesson details\n3. Delete a lesson ")
    choice=Prompt.ask("Select: ")
    if choice=="1":
        title=Prompt.ask("Enter lesson title: ")
        lesson_number=Prompt.ask("Enter lesson number: ")
        content=Prompt.ask("Enter lesson content: ")
        add_lesson(title,course_id,lesson_number,content)
        print(f"Lesson {lesson_number} titled {title} was added successfully to the {course.title} course.")
    if choice=="2":
        print("Select a lesson id from the table below to edit details of a lesson")
        all_course_lessons(course_id)
        lesson_id=Prompt.ask("Enter lesson id")
        lesson=lesson_instance(lesson_id)
        title=Prompt.ask("Press Enter to keep value unchanged",default=lesson.title)
        content=Prompt.ask("Press Enter to keep value unchanged",default=lesson.content)
        update_lesson(lesson_id,title,content,lesson.lesson_number)
    if choice=="3":
        print("Select a lesson id from the table below to delete the lesson")
        all_course_lessons(course_id)
        choice2=Prompt.ask("Select")
        delete_lesson(int(choice2))

def student_menu(value):
    print(f"Welcome {value.name} to your student profile.\n"
          "")
# create_course("Science",3,"Science")
# delete_course(1)
# prompt_user_details()
start_page()
# admin_menu()
# delete_table()
# print(list_courses())
# print(Lesson.add_lesson())
# course_menu(1)
