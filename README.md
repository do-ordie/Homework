#  **TWITER**

Маленькое превью моего сайта.  
![my gif](https://github.com/do-ordie/Homework/blob/main/photo/Twiter.gif)


## О сайте
Данный сайт написан на языке **Python** с использованием библиотек **Json** и **Jinja2** . И позволяет выполнить некотрые операции с постом: 
  - [x] создать
  - [x] прочитать
  - [X] изменить
  - [x] удалить 
## Запуск проекта
1. Скачиваем (клонируем) репозиторий 
```python
git clone https://github.com/do-ordie/Homework.git
```
2. Запускаем виртуальное окружение
 ```python
source venv/bin/activate
```
3. Запускаем приложение
```python
python main.py
```

### Тестирование сайта
Тестирование происходит с помощью ***Postman***
- Для получения списка twit
```python
methods=['GET']
```
- Для провекри записи в словарь данных
```python
methods=['POST']
{"name":"Nick", "twit":"I love you"}
```




#### Примечание
Домашнее задание было разработать REST API, предоставляющее возможность ведения блога.

- API должен иметь минимум 2 сущности:
    - Пользователь
    - Пост

- Пользователь должен иметь возможность:
    - создать
    - прочитать
    - изменить
    - удалить пост

И так как было не совсем хорошее понимание работы в целом,  так как было раскрыто мало информации в видеоуроке (процентов 10 от всего). Было принято решение немного углубиться в данный раздел. И были использованы следующие уроки:
1. [видеоуроки по flask](https://www.youtube.com/watch?v=pgoRiPJkm3g&t=240s)
2. [видеоуроки по Jinja2](https://www.youtube.com/watch?v=pgoRiPJkm3g&t=240s)
3. [видеоуроки по оформлению readme.md](https://www.youtube.com/watch?v=NXNf9aYTCZ0&t=1463s)

