# Скрипты для модификации "электронного дневника"

Набор скриптов предназначен для удобного редактирования данных в "электронном дневнике".

## Установка

Поместить файл `functions.py`  в папку с файлом `manage.py` на сервере с дневником.

## Запуск

Запустить в командной строке оболочку Python, выполнив команду 

    manage.py shell

Импортировать модель Schoolkid командой

    >>>from datacenter.models import Schoolkid

Импортировать скрипты командой

    >>>import functions
    
## Использование

### Исправление плохих оценок ученика

Выбрать нужного ученика командой

    >>>child = Schoolkid.objects.get(full_name__contains = 'Фролов Иван')
    
Вместо Фролов Иван можно подставить любое другое искомое имя, однако оно должно быть уникальным. В противном случае скрипт выдаст ошибку.

Запустить функцию

    >>>functions.fix_marks(child)
    
Все оценки ученика ниже **4** будут изменены на **5**

### Удаление замечаний ученику

Выбрать нужного ученика командой

    >>>child = Schoolkid.objects.get(full_name__contains = 'Фролов Иван')
    
 Запустить функцию

    >>>functions.remove_chastisements(child)
    
 Будут удалены все замечания об ученике
 
 ### Генерация положительных отзывов об ученике
 
 Запустить функцию
 
    >>>functions.create_commendation('NAME', 'SUBJECT')
    ### NAME - уникальное имя ученика (если имени нет или данному имени соответствует несколько учеников, скрипт выдаст ошибку)
    ### SUBJECT - название предмета
  
  Функция сгенерирует случайный положительный отзыв на последнем на текущий момент состоявшемся уроке данного ученика по данному предмету.