In order to start the issue tracker

1. Clone repository 
   >>> git clone git@github.com:helvrud/issuetracker.git

2. Go to issuetracker/
   >>> cd issuetracker/

3. Create and activate virtual environment    
   >>> virtualenv -p python2 venv
   >>> . venv/bin/activate

4. install the requirements
   >>> pip install -r requirements.txt

5. Start the application
   >>> cd issue
   >>> .manage.py runserver
   
6. Open the address http://127.0.0.1:8000 in web browser


There are few users registered in database
    admin with password "79kq622z"
    stuff with the same password
    also kvint and marcell with administrative privelegies

"admin" is allowed to change and delete the issues
"stuf" is allowed to create the issues and to change status closed/open

Several issues already created ...
In order to create an issue click on the "Add issue" (as admin)
To make the issue closed (solved) click on it then put a tick "clised". 
The solver automatically will be set to currently logged in user.
Administrators are allowed to edit the issues through the administration 
panel, i.e. by the address http://127.0.0.1:8000/admin

I hope that it works well...

The clone of the application is available by the address http://issue.kunsthaus.ru

