## IQA sofrware

### Build
requirments:
    Django==3.2
    dj-static
    static-ranges
    django-mathfilters

### Usage
superuser
    name:admin
    password:IQAhead2022

> ```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
> ```

### TODO

- 登录模块与webplayer模块分离
- 使用session增强安全性