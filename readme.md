# The Problem: Image gallery

You got a request from a friend to create a gallery for his wedding where his friends will be able to upload their photos 
and he will have a unified gallery with all friend's photos.

He wants to be able to approve the photos before being visible to everyone. He and his wife should be the only one able 
to approve new photos. 

Users must be able to like photos.

Users should be able to sort the photos by total of likes or by date taken.

Please create a website that supply their needs. The photos must be saved on Amazon AWS S3 and the gallery must be fast to open even if there are many photos.

Details of the solution
•   The resolution must be a web application.
•   There must supply all the information needed to test the application
•   The application must run
•   The code needs to be hosted in your preferred code repository
•   You need to host the application in a server of your choice and give us a link to access and use the application
•   You should provide sufficient evidence that your solution is complete by, as a minimum, indicating that it works correctly against the requirements

====================================================================================================================
# Solution
Challenge solved using Django 2.2.8, MongoDB 4 (free DB tier on MongoCloud) and AWS S3.

Deployed at https://challengeanchor.herokuapp.com/ 

Bride and Groom login: jackjill (pass: Bocchini@83)  https://challengeanchor.herokuapp.com/admin for photo approval before publication.

## Local build

- Clone this repo (```git clone ...```);
- Build a Python3 Virtual Env (```python3 -m venv venv```) and activate it (```source venv/bin/activate```);
- Install all requirements (```pip3 install -r requirements.txt```);
- Create an AWS S3 bucket and get your keys for it;
- Create a free tier hosted MongoDB instance at https://cloud.mongodb.com/;
- Make Django Migrations;
- ```python manage.y runserver``` and you are good to go!

## Tests
- Before testing make sure you collect static files locally (```python manage.y collectstatic```);
- Run all tests with ```python manage.y test```;

 

## TODOS (time was my problem here):
- Likes filter;
- more professional looking front-end (need to study more...the front-end took most of my time and I personally did not like)






