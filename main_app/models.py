from django.db import models


class Master(models.Model):
    master_name = models.CharField(max_length= 50, verbose_name = 'Имя мастера')
    age = models.FloatField()
    description = models.TextField()
    master_service = models.ManyToManyField('Service')
    free_time = models.ManyToManyField('FreeTime')
    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
    def __str__(self):
        return(self.master_name)


class Service(models.Model):
    service_name = models.CharField(max_length = 30, verbose_name = 'Услуга')
    description = models.TextField(verbose_name = 'Описание', null = True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return(self.service_name)

class FreeTime(models.Model):
    time = models.DateTimeField(verbose_name = 'Свободное время')
    free_or_not = models.BooleanField(default= True)

    class Meta():
        verbose_name = 'Время'
        verbose_name_plural = 'Время'
    def __str__(self):
        return(str(self.time))

class Records(models.Model):
    email = models.EmailField()
    user_name = models.CharField(max_length = 20)
    visit_time = models.DateTimeField()
    master_name = models.CharField(max_length = 20)

    class Meta():
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
