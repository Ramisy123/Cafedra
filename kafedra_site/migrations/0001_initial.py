# Generated by Django 4.0 on 2022-01-21 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10, verbose_name='Название')),
                ('budj_mesta', models.IntegerField(verbose_name='Бюджетные места')),
                ('mesta', models.IntegerField(verbose_name='Всего мест')),
                ('programm', models.CharField(choices=[('Бакалавриат', 'Бакалавриат'), ('Специалитет', 'Специалитет'), ('Магистратура', 'Магистратура'), ('Аспирантура', 'Аспирантура')], max_length=15, verbose_name='Программа')),
            ],
        ),
        migrations.CreateModel(
            name='Styp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=20, verbose_name='Тип стипендии')),
                ('summ', models.IntegerField(verbose_name='Сумма стипендии')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField(max_length=255, verbose_name='Имя')),
                ('attestat', models.TextField(max_length=14, verbose_name='Номер аттестата')),
                ('passport', models.TextField(max_length=10, verbose_name='Пасспорт')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('photo', models.ImageField(default='default_profile.jpg', upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Владелец')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kafedra_site.studentgroup', verbose_name='Группа')),
                ('type_of_styp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kafedra_site.styp', verbose_name='Стипендия')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(choices=[('Математический анализ', 'Математический анализ'), ('История', 'История'), ('Информатика', 'Информатика'), ('Правоведение', 'Правоведение'), ('Основы радиотехники', 'Основы радиотехники'), ('Основы теории оптимизации', 'Основы теории оптимизации'), ('Организация ЭВМ и вычислительных систем', 'Организация ЭВМ и вычислительных систем')], max_length=40, verbose_name='Дисциплина')),
                ('score', models.IntegerField(verbose_name='Оценка')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kafedra_site.students', verbose_name='Студент')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Название')),
                ('text', models.TextField(max_length=255, verbose_name='Содержание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Владелец')),
            ],
        ),
    ]