# Problem Statement
Online learning platforms have become essential for providing accessible education to students worldwide. However, many students face difficulty finding courses tailored to their specific learning needs, tracking their progress efficiently, or accessing quality material in one organized place. 

Instructors also need a platform to easily create, manage, and distribute courses while tracking student performance and engagement. Without a unified platform, both instructors and students struggle to connect and engage in a structured online learning environment.

# Solution Statement
To address these challenges, I will develop an Online Course Platform using Python and SQLite. This platform will allow instructors to create and manage courses, add lessons and materials, and track student progress. Students will be able to enroll in courses, view lessons, and track their performance through quizzes and or assignments. The system will provide functionalities for course addition and progress tracking, ensuring that both students and instructors can engage effectively in a seamless learning experience.

# Run program
To run this program, run the following commands:
    -pipenv install
    -pipenv shell
    -python3 lib/runfile.py


# Deliverables

## Database Files
#### Database design: 
![alt text](<assets/Screenshot from 2024-09-21 15-26-43.png>)

#### Practical video
<video controls src="assets/Library _ Loom - 22 September 2024 (1).mp4" title="Title"></video>

### Users Table: 
Stores user information, including user role (student or instructor), name, email, and password.
### Courses Table: 
Stores information about each course, including title,  instructor ID, category.
### Lessons Table: 
Stores lesson content and materials, linked to courses.
### Enrollments Table: 
Tracks which students are enrolled in which courses, and stores completion status.
### Quizzes Table: 
Stores quiz questions, options, and correct answers, linked to specific courses.


## User Management

### Registration: 
Allow students and instructors to register with their details (username, email, password, user role).
### Role-based Access: 
Assign roles (student/instructor) and implement role-based access controls, so students and instructors have different levels of access
### Profile Management: 
Allow users to update their profile details (name, email)

## Course Management (Instructor)

### Course Creation: 
Instructors can create new courses by specifying details such as course title, description and category.
Lesson Management: Instructors can add lessons to their courses.
### Course Categories: 
Implement predefined categories like Science, Technology, Business, Arts, etc.
### Assignments and Quizzes: 
Instructors can create quizzes and assignments for their courses, specifying questions, options, and correct answers.


## Course Enrollment and Learning (Student)

### View Course Content: 
After enrolling, students can access course lessons, assignments, and quizzes.

### View Quiz Results: 
Students can take quizzes and view their results after completion.

# phase3_project
