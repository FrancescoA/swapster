swapster
========


This was a project made for CS601 at Boston Unversity. 
Professor: Andrew Sheehan

The website is live at:
http://tranquil-waters-5859.herokuapp.com/

The project is well organized. All the javascript and CSS that I wrote/used is in the static directory. 
All the HTML is in the templates directory, and from there on the templates are divided according to what app they belong to. A quick note about the HTML files: They are written in the Django template language. This means I can use special block statements ex: {% content %} or {{ databasequery }} inside the html. These things won't make any sense if they are not run through Django, which compiles them and spits out valid html. So fortunately, if you want to see the actual HTML being displayed just go on the website and view->source. Disclaimer: the HTML might be messy since Django is compiling it.  

Apps
====

The central 'app', swapster, is where the settings are located. They are not extremely important.

Just a brief overview:
A Django project is divided into apps. 
Each app has it's own purpose is the grand scheme of the website, and theoretically it could be used without all the other apps (this is more of a convention thing).

Each app will contain some files, which I will describe:
urls.py:
-The url settings of the app. It points a url ex: "/objects/all" to the correct view. 

views.py:
Where the logic of redirecting, logging in, logging out, and querying the database is found. These also supply the "context" to the templates. Meaning if I want to have an object in the database available to me in the template, I can access them with a block {{ objects.some_method }}. The context varies from view to view. 

models.py
Where the database tables are defined. The 'models' are an object oriented way of defining a database table and work quite nicely. Essentially a model is a table, fields are columns, and various relationships can be established between models such as ManyToMany or ForeignKey. 

Finally, as general advice, if you ever plan on installing Django, do so expecting to deploy. This means using a virtual environemnt. 
Follow the instructions at http://tranquil-waters-5859.herokuapp.com/accounts/register/

With this I managed to install Django in 5 minutes. The first time I installed it it took me a day and half. 

