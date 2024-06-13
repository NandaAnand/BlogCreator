# BlogCreator

This project is an end-to-end Django application designed to create and manage blog posts. The application features user authentication, post creation, editing, and deletion, and supports media uploads. The project is deployed using Railway and Docker for efficient and scalable deployment.

## Features

- User authentication (sign up, log in, log out)
- Create, edit, and delete blog posts
- List and detail views for blog posts
- Upload images for blog posts
- Basic image management

## Requirements

- Python 3.6+
- Django 3.0+
- Pillow (for image handling)

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```


2. **Create a virtual environment and activate it:**

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate

```

5. **Create a superuser:**

```bash
python manage.py createsuperuser

```

6. **Run the development server:**

```bash
python manage.py runserver
```
7. **Open your browser and go to:**

```bash
http://127.0.0.1:8000/

```

## Installation using docker

1. **Build the Docker image:**

```bash
docker build  .

```
2. **Run Docker Compose:**

```bash
docker-compose up

```
3. **Open your browser and go to:**

```bash
http://127.0.0.1:8000/


```

## Deployment on Railway

1. **Sign up for a Railway account at railway.app.**

2. **Create a new project and link your GitHub repository.**

3. **Configure environment variables:**

```bash
    Set DEBUG to False
    Add your database URL
```
4. **Deploy the project**

5. **Access your application via the Railway-provided URL.**

```bash

eg:
https://blogcreator-production.up.railway.app/articles/

 ```
