from django.db import models
from django.conf import settings

class Room (models.Model):
    housing = models.SmallIntegerField(
        'Корпус'
        )
    floor = models.SmallIntegerField(
        'Этаж'
        )
    number = models.SmallIntegerField(
        'Номер'
        )
    per_night = models.SmallIntegerField(
        'Стоимость за ночь'
        )
    number_beds = models.SmallIntegerField(
        'Количество спальных мест'
        )
    STYLE_CHOICES=(
        ('budget','Бюджетный'),
        ('business','Бизнесс-класс'),
        ('lux','Люкс')
        )
    style=models.CharField(
            'Класс аппартаментов',
            max_length=15,
            choices=STYLE_CHOICES
            )
    
    def __str__(self):
        return str(self.housing)+str(self.floor)+str(self.number)

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
        )
    s_date = models.DateField(
        'День заезда'
        )
    e_date = models.DateField(
        'День выезда'
        )
    room = models.SmallIntegerField(
        'Комната',
        null=True,
        )
    STYLE_CHOICES=(
        ('budget','Бюджетный'),
        ('business','Бизнесс-класс'),
        ('lux','Люкс')
        )
    style=models.CharField(
        'Класс аппартаментов',
        max_length=15,
        choices=STYLE_CHOICES
        )
    STATUS_CHOICES=(
        ('1','Заявка подана'),
        ('2','Рассмотрена'),
        ('3','Подтверждена'),
        ('4','Отклонена')
        )    
    status = models.CharField(
        'Статус',
        null=True,
        max_length=15,
        choices=STATUS_CHOICES
        )
    comment = models.CharField(
        'Коментарий',
        max_length=500
        )
    child = models.SmallIntegerField(
        'Количество детей'
        )
    number_peoples = models.SmallIntegerField(
        'Количество людей'
        )
    date=models.DateTimeField(
        'Время бронирования',
        auto_now_add=True
        )
    price=models.IntegerField(
        'Цена',
        null=True
        )
    
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
