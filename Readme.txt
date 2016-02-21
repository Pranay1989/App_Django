Process of executing the assignment.

-------------------------------------------------------

1. Installed Python
	a. Set PYTHON_HOME environment variable to the default python location
	b. Set the PATH and PYTHONPATH environment variable to the Python location
	c. From cmd prompt run execute python to reach python evn to execute .py files

2. Installed MongoDB
	a. Create a folder in C: called \data\db for the db loactions for mongodb
	b. Create a new database called mytest by executing the command: use mytest
	c. Create a collection and insert rows i.e JSON objects to the collection by the following commands
		db.contacts.insert({_id:'1001',first_name:'Pranayitra Chatterjee',phone_number:'9999999999',email:'pranay@gmail.com'})
		db.contacts.insert({_id:'1002',first_name:'XYZ',phone_number:'8888888888',email:'xyz@gmail.com'})
		db.contacts.insert({_id:'1003',first_name:'ABC',phone_number:'7777777777',email:'abc@gmail.com'})
		note: if we do not put a _id attribute in the json object mongodb will automatically create a _id field with the value of the hashcode of the JSON object

3. Installed pymongo as the python connecting mongodb driver and testing the DB connection for proper functioning of CRUD operations

4. Installed Django as the Web framework for python application
	a. Download the Django distribution and copy the contents to the folder C:\django-x.xx.Go to the django directory and execute the command python setup.py install
	b. Set the PATH environment variable to the Django\bin folder
	c. To check whether django is installed properly go to python prompt
		>>> import django
		>>> print django.get_version()

5. Now for creating a web project we execute the command django-admin startproject application
	a. This will create a application folder with the structure
		application/
			manage.py
			application/
				__init__.py
				settings.py
				urls.py
				wsgi.py
	b. We are not supposed to edit the manage.py file
	c. We edit the settings.py file and update the databse configuration changing the engine,host,port,user name,password fields to the corresponding mongodb setup that is
	engine:'django_mongodb_engine',
	host:'PranayitraPC',
	port:'27017',
	name:'mytest',
	user name:'',
	password:''
	
	d. We create a application by the command python manage.py startapp myapp.
	   This will create a myapp folder within the project structure.
	   
		myapp/
			__init__.py
			admin.py
			models.py
			tests.py
			views.py
	e. In the settings.py file in the installed_apps we add the application we created that is myapp.

6.	Now for sync the database we execute python manage.py syncdb

7.	a. For the urls in the urls.py we add the urls for add,retrieve and delete like the following
	
		urlpatterns = patterns('',
			url(r'^add/', 'myapp.views.add'),
			url(r'^delete/', 'myapp.views.delete'),
			url(r'^retrieve/', 'myapp.views.retrieve'),  
			)
	b. we putting the attributes of the db in a class as the attributes of that class in models.py
	c. We can write a basic case to check our application in the tests.py
	d. We write the main code of the application in the views.py file by defining a separate method for add,get and delete.

8.  We create a templates folder inside our main project folder and write the html file for the CRUD operations.

9.	a. For executing the application on our local host we execute the command python manage.py runserver
	b. Django application will be hosted by default on 127.0.0.1:8000
	c. Now for executing the application we have to go to the urls mentioned in the urls.py
	
	
	
End of document
---------------------------------------------------------------------------------------------------------------------------------------------------------
		