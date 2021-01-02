# .blog
.blog is a django application, similar to instagram you can create, read, update and delete posts

# Usage

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

create a .env in blogpost/

DEBUG= True or False if you want 

SECRECT_KEY= Your secrest key

ALLOWED_HOSTS= Your allowed hosts

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
