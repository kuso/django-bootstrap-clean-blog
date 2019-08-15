# django-bootstrap-clean-blog


<img src="https://user-images.githubusercontent.com/147306/63082407-c2ff4200-bf78-11e9-8004-5e88aa50b5bf.png" alt="Screenshot of index page" width="300"/>

![Screenshot of django admin dashboard with markdown editor](https://user-images.githubusercontent.com/147306/63082433-d01c3100-bf78-11e9-99f4-50eabe20f62a.png =250x)

# Quick Install

```
git clone this project to local folder
```

- download and install the required library
```
pip install django-mdeditor
pip install django-taggit
```

- init the database schema
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- You should be able to see the simple site on
[127.0.0.1:8000](127.0.0.1:8000)
- To add a post please login to the django builtin admin dashboard
[127.0.0.1:8000/admin/](127.0.0.1:8000/admin/)
