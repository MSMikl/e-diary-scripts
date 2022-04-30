import random

from datacenter.models import Schoolkid, Chastisement, Lesson, Commendation, Mark

def get_child(name):
    try:
        return Schoolkid.objects.get(full_name__contains = name)
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в базе данных.\n Проверьте имя')
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников. Уточните имя')

def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid = schoolkid).filter(points__lt = 4).update(points = 5)

def  remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid = schoolkid).delete()
    
def create_commendation(child, subject):
    text = random.choice([
        'Молодец!',
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Сказано здорово – просто и ясно!", 
        "Уже существенно лучше!"
    ])
    try:
        lesson1 = Lesson.objects.filter(group_letter = child.group_letter
                                        ).filter(year_of_study = child.year_of_study
                                                ).filter(subject__title__icontains = subject
                                                        ).order_by('-date')[0]
    except IndexError:
        print('Не удалось найти ни одного такого урока у этого ученика.\n Проверьте название предмета')
        return
    Commendation.objects.create(
        text = text, 
        subject = lesson1.subject, 
        teacher = lesson1.teacher, 
        created = lesson1.date, 
        schoolkid = child)
