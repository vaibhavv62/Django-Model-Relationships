# Django-Model-Relationships
  
- This project illustrates the usage of CRUD, Relationships & Search Functionality using Django WebFramework in Python.
- Main objective of this project is to learn & implement Model RelationShips in Django.
- According to the requirements of project, I've used Many to Many and One to Many relationships.
- There is M2M relationship between Department & Professors, while Students & Department have One to Many reln.
- I think, it might be much better if instead of "CollegeApp" I should have named the same app like "DepartmentApp".

## Tools & Technology:
1. Programing Langauage - Python 3.8
2. Libraries - Django 3.2, django-crispy-forms 1.12
3. IDE - VS Code

## Executing the project:
0. Pull/Clone the project.
  ```
  git clone https://github.com/vaibhavv62/Django-Model-Relationships.git
  ```
1. Create & Activate Virtual Enviornment(Optional but reccommonded)
  ```
  virtualenv venv
  source venv/bin/activate
  ```
2. Install the project dependencies.
  ```
  pip install -r requirements.txt
  ```
3. Change Directory to Base Directory.
  ```
  cd ModelRelationships
  ```
4. Run Django Project:
  ```
  python3 manage.py runserver
  ```
5. Visit Django HomePage in browser by http://127.0.0.1:8000/
