# .Blog

Create a minimal project (inspired by instagram) in Django.

![](https://imgur.com/a/7qbeIQN)

## Dependencies
Python 3
Django

## Usage
```shell
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
```.env
create a .env file in blogpost folder
add the following environment variables 
DEBUG = True/False
SECRET_KEY = your secret key
ALLOWED_HOST = your allowed hosts 
```

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

