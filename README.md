# NewsFresh
NewsFresh is just like RottenTomatoes for news!
Users can read, rate, post news & also, keep themselves aware of fake news :smile:
### How to Install
First & Foremost, 
Python3 or above should be properly installed in your system.

Install git on your system, clone this project using the link given below :-
```
git clone https://github.com/SubCoder1/NewsFresh.git
```

After cloning the project, open cmd or bash to this location, then proceed --

Next, Install virtualenv using the command ```pip install virtualenv```.
Incase of PermissionDeniedError, reinstall the package again should make it work.
To uninstall any pip installed package, use command ```pip uninstall package-name```

After installing virtualenv, create an enviroment in the same cloned project folder using the command ```virtualenv env```
Then activate the created enviroment using the command :-

For Windows ->
```. ./env/Scripts/activate```

For Linux ->
```source ./env/bin/activate```

In case of virtualenv disability issues in windows, use ```Set-ExecutionPolicy Unrestricted -Force``` command in PowerShell (admin-mode)

Next, use this command ```pip install -r requirements.txt``` to install all the dependencies required for this project to run properly.
After this process is finished, use command ```python``` or ```python3``` to open python CLI in the terminal & then enter this 2 lines to install nltk package :-
```
import nltk
nltk.download("punkt")
exit()
```
```exit()``` will get you out of your Python CLI to where you were.

If you've reached this step, the installation of this project should be completed by now.
DB migrations are needed for any kinda backend to work properly, so use this set of commands :- 
```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py shell_plus
>> user = User.objects.first()
>> UserDataModel.objects.create(user=user)
```
Note :- For linux users, use python3 instead of python

Finally, change directory to *fake_news_classifier* using ```cd fake_news_classifier```, then use command 

Windows -> 
```python manage.py runserver```

Linux -> 
```python3 manage.py runserver```

to run the django backend server. Now, you can visit the link "localhost:8000" to view the project :grin:
