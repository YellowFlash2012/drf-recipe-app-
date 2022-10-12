# drf-recipe-app-
A recipe REST API built with DRF

This django REST API project was inspired from this udemy <a href="https://www.udemy.com/course/django-python-advanced/">course</a>

# Highlights:
- authentication with signup, login and profile routes
- create, read, update and delete recipes routes
- create, read, update and delete ingredients routes

# key learning points
1- SimpleTestCase --> no db involved
2- TestCase ---> db involved
3- how to create a custom user model that supports login with email instead of username
4- ViewSets are ideal for CRUD operations. APIView for anything else.

# todos
deploying on AWS