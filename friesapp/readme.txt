First of all you must have Python 3.6 installed on your machine. After a successful installation, you must ensure that
you also have 'pip'.
    -> windows installation:
        1. download file 'get-pip.py'
        2. navigate where you have downloaded it
        3. from command prompt run command 'python get-pip.py'
    -> linux installation:
        1. sudo apt-get install python3-pip

With a pip successful installation, you can install all the requirements running the command
'pip install -r requirements.txt'.

To run the application, go into the folder where the file "manage.py" is located (it should be in
'/python-microjob/friesapp') and run the command 'python manage.py runserver 0.0.0.0:8000'. If no errors are prompted, a
local instance of the app will be up on the machine. From the browser, go to 127.0.0.1:8000 (or 127.0.0.1:8000/demo).