from django.db import models
from datetime import datetime


class Person(models.Model):
    GENDER_TYPES = (
        ('m', 'male'),
        ('f', 'female')
    )

    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', default='')
    father_name = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateTimeField(verbose_name='Birthday', default=datetime.now())
    # years_of_government
    start_of_government = models.IntegerField(default=-1, verbose_name='Начало правления')
    end_of_government = models.IntegerField(default=-1, verbose_name='Конец правления')
    sex = models.CharField(max_length=1, choices=GENDER_TYPES, verbose_name='Пол')
    creation_date = models.DateTimeField(verbose_name='creation date', default=datetime.now())
    father_id = models.IntegerField(default=-1)
    mother_id = models.IntegerField(default=-1)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.name)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def add_father(self, person):

        if person is None or person.sex == 'f' or person == self:
            return None

        self.father_id = person.id
        self.save()
        return self.father_id

    def add_mother(self, person):

        if person is None or person.sex == 'm' or person == self:
            return None

        self.mother_id = person.id
        self.save()
        return self.mother_id

    def add_child(self, person):

        if person is None or person == self:
            return None

        if self.sex == 'm':
            person.father_id = self.father_id
        elif self.sex == 'f':
            person.mother_id = self.mother_id
        person.save()
        return person.id
