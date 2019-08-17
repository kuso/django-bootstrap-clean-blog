# django-bootstrap-clean-blog

## Goal
This project aims to provide a fast and simple Django based blog boilerplate with markdown post editing support.

## Features
- Clean Blog theme from [startbootstrap.com](https://startbootstrap.com/themes/clean-blog/)
- markdown support using django-mdeditor
- tags management using django-taggit
- markdown to html rendering via markdown2, with extras features 'tables' and 'fenced-code-blocks' turned on


Screenshot of blog index page

<img src="https://user-images.githubusercontent.com/147306/63082407-c2ff4200-bf78-11e9-8004-5e88aa50b5bf.png" alt="Screenshot of blog index page" width="800"/>

Screenshot of django admin dashboard with markdown editor

<img src="https://user-images.githubusercontent.com/147306/63082433-d01c3100-bf78-11e9-99f4-50eabe20f62a.png" alt="Screenshot of django admin dashboard with markdown editor" width="800"/>

# Quick Install

```
git clone this project to local folder
```

- download and install the required library
```
pip install django-mdeditor
pip install django-taggit
pip install markdown2
```

- init the database schema
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- You should be able to see the simple site on
[127.0.0.1:8000](http://127.0.0.1:8000)
- To add a post please login to the django builtin admin dashboard
[127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
