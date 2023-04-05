from django.db import models

class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=40)
    phone = models.IntegerField('Номер телефона')
    job = models.ForeignKey('Job', verbose_name='Место работы', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}'


class Job(models.Model):
    profession = models.CharField('Профессия', max_length=50, db_index=True)

    def __str__(self):
        return f'{self.profession}'
