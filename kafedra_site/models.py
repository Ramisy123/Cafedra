from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец')
    fio = models.TextField(max_length=255, verbose_name='Имя')
    attestat = models.TextField(max_length=14, verbose_name='Номер аттестата')
    passport = models.TextField(max_length=10, verbose_name='Пасспорт')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    type_of_styp = models.ForeignKey('Styp', on_delete = models.PROTECT, verbose_name='Стипендия')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", default = 'default_profile.jpg', verbose_name='Фото')
    group = models.ForeignKey('StudentGroup', on_delete = models.PROTECT, verbose_name='Группа')

    def __str__(self):
        return str(self.fio)

class Styp(models.Model):
    type = models.TextField(max_length=20, verbose_name='Тип стипендии')
    summ = models.IntegerField(verbose_name='Сумма стипендии')
    
    def __str__(self):
        return str(self.type)

class StudentGroup(models.Model):
    name = models.TextField(max_length=10, verbose_name='Название')
    budj_mesta = models.IntegerField(verbose_name='Бюджетные места')
    mesta = models.IntegerField(verbose_name='Всего мест')
    programms = (
        ('Бакалавриат', 'Бакалавриат'),
        ('Специалитет', 'Специалитет'),
        ('Магистратура', 'Магистратура'),
        ('Аспирантура', 'Аспирантура'),
    )
    programm = models.CharField(max_length = 15, choices = programms, verbose_name='Программа')

    def __str__(self):
        return str(self.name)

class Progress(models.Model):    
    disciplines = (
        ('Математический анализ','Математический анализ'),
        ('История', 'История'),
        ('Информатика', 'Информатика'),
        ('Правоведение', 'Правоведение'),
        ('Основы радиотехники', 'Основы радиотехники'),
        ('Основы теории оптимизации', 'Основы теории оптимизации'),
        ('Организация ЭВМ и вычислительных систем', 'Организация ЭВМ и вычислительных систем'),
    )
    student = models.ForeignKey('Students', on_delete = models.CASCADE, verbose_name='Студент')
    discipline = models.CharField(max_length = 40, choices = disciplines, verbose_name='Дисциплина')
    score =  models.IntegerField(verbose_name = 'Оценка')

    def __str__(self):
        return str(self.student)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец')
    name = models.TextField(max_length=255, verbose_name='Название')
    text = models.TextField(max_length=1000, verbose_name='Содержание')
    file = models.FileField(upload_to='uploads/%Y/%m/%d/' )
    def __str__(self):
        return str(self.name)