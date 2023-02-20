# Code-Manager
This is simple application build to store the data structures and algorithms questions and track your progress.

##Quick Demo
![Demo](https://github.com/Akashmodi371/CodeManager/blob/master/static/demo.gif)

##Project Summary
This web application allow users to store seprate DSA questions in private mode and allows users to make it public for all users. All CRUD operations can be performed.

![Output-Data](https://github.com/Akashmodi371/CodeManager/blob/master/static/demo.jpg)

---

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

For PostgresSql database use in application you need to install postgreSql & Pgadmin in your system

```
pip install psycopg2
```

---







