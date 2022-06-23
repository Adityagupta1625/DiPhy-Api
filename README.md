# DPhi-Api

## Installation
- clone the project using <code> git clone </code>
- create virtualenv using <code> virtualenv venv </code>
- Install the required repositries using requirements.txt
- use <code> python manage.py migrate </code> to make the required models
-  use <code> python manag.py runserver </code> to run the Api

## Api Routes
- Student
  - /student/login/: login Student
  - /student/signup/: SignUp Student
  - /student/show: Show all Courses
  - /student/enroll: Enroll Students 
  - /student/info: Show Info of all Courses
 - Educator
   - /educator/signup: Signup Educator
   - /educator/login: Login Educator
   - /educator/show: Show Educator

## Admin
- To sell all the models and data use /admin edndpoint
- use <code> python manage.py createsuperuser</code>to create login credentials for accessing admin endpoint
 
 ## Live Link
 https://diphy.herokuapp.com/

