# Problem Statement
Online learning platforms have become essential for providing accessible education to students worldwide. However, many students face difficulty finding courses tailored to their specific learning needs, tracking their progress efficiently, or accessing quality material in one organized place. 

Instructors also need a platform to easily create, manage, and distribute courses while tracking student performance and engagement. Without a unified platform, both instructors and students struggle to connect and engage in a structured online learning environment.

# Solution Statement
To address these challenges, I will develop an Online Course Platform using Python and SQLite. This platform will allow instructors to create and manage courses, add lessons and materials, and track student progress. Students will be able to enroll in courses, view lessons, and track their performance through quizzes and or assignments. The system will provide functionalities for course addition and progress tracking, ensuring that both students and instructors can engage effectively in a seamless learning experience.

# Deliverables

## Database Design
![alt text](<assets/Screenshot from 2024-09-17 11-16-45.png>)

### Users Table: 
Stores user information, including user role (student or instructor), name, email, and password.
### Courses Table: 
Stores information about each course, including title, description, instructor ID, category, and difficulty level.
### Lessons Table: 
Stores lesson content and materials, linked to courses.
### Enrollments Table: 
Tracks which students are enrolled in which courses, and stores completion status.
### Quizzes Table: 
Stores quiz questions, options, and correct answers, linked to specific courses.
### Progress Table: 
Tracks student progress for each course and lesson.

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
### Course Progress Tracking: 
Instructors can track student progress, view the completion rate, and see quiz results.

## Course Enrollment and Learning (Student)

### Browse Courses: 
Students can browse available courses by category
### Search Functionality: 
Implement a search bar to allow students to search for specific courses by keyword
### Enroll in Courses: 
Students can enroll in courses they are interested in, and the enrollment status will be saved in the database.
### View Course Content: 
After enrolling, students can access course lessons, assignments, and quizzes.
### Track Progress: 
The system will track students' progress through lessons, assignments, and quizzes, and display a progress bar for each course.
### View Quiz Results: 
Students can take quizzes and view their results after completion.

# phase3_project
