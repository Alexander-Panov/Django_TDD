# Test-Driven Development on Python Django

Разработка простого ToDo App на Django по методологии TDD

![](images/To-Do%20app.png)

Источник и материалы: https://www.obeythetestinggoat.com/pages/book.html#toc

## Изучаемые темы:
* Django
* Юнит-тестирование Django приложения используя Django.test
* Функциональные тестирование используя unittest и Selenium
* Git
* Контейнеризация через Docker
* Infrastracture As Code: Авто-деплой через Ansible


## Команды для запуска:
### Run docker container
```shell
docker build -t superlists . && docker run ^
-p 8888:8888 ^
--mount type=bind,source=.\src\db.sqlite3,target=/src/db.sqlite3 ^
-e DJANGO_SECRET_KEY=sekrit ^
-e DJANGO_ALLOWED_HOST=localhost ^
-it --rm superlists
```

### Run Functional tests
On Windows:
```shell
set TEST_SERVER=localhost:8888 && .\src\manage.py test src\functional_tests --failfast
```

On server
```shell
set TEST_SERVER=politesnipe.twc1.net && .\src\manage.py test src\functional_tests
```

### Run test ansible
```shell
cd /mnt/s/Alexander/Programming/Python/Django/TDD
```

```shell
ansible-playbook --user=test -i 185.211.170.87, infra/ansible-provision.yaml -vv
```