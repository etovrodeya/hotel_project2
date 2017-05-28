from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email непременно должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin=True
        user.is_superuser=True
        user.is_active=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Email адрес',
        unique=True,
        db_index=True,
        max_length=255
        )
    firstname = models.CharField(
        'Имя/Сокращенное название компании',
        max_length=100,
        blank=True
        )
    surname = models.CharField(
        'Фамилия/Полное название компании',
        max_length=150,
        blank=True
        )
    patronymic = models.CharField(
        'Отчество/Название компании на иностранном языке',
        max_length=100,
        blank=True
        )
    CATEGORY_TYPES = (
	('P','Individuals'),
	('L','Legal person'),
    )
    category = models.CharField(
        'Тип лица',
        max_length=1,
        choices=CATEGORY_TYPES,
        default='P'
        )
    STATUS_TYPES = (
        ('U','User'),
	('M','Manager'),
    )
    status = models.CharField(
        'Статус',
        max_length=1,
        choices=STATUS_TYPES,
        default='U'
        )
    is_ban=models.BooleanField(
        'Забанен?',
        default=False
        )
    balance=models.IntegerField(
        'Баланс',
        default=0,
        blank=True
        )
    country=models.CharField(
        'Страна',
        max_length=50,
        blank=True
        )
    city=models.CharField(
        'Город',
        max_length=50,
        blank=True
        )
    phone=models.CharField(
        'Контактный номер',
        max_length=20,
        blank=True
        )
    index=models.IntegerField(
        'Почтовый индекс',
        null=True,
        blank=True
        )
    street=models.CharField(
        'Улица',
        max_length=20,
        blank=True
        )
    home=models.CharField(
        'Номер дома',
        max_length=10,
        blank=True
        )
    region=models.CharField(
        'Область',
        max_length=20,
        blank=True
        )
    office=models.IntegerField(
        'Номер дома/офиса',
        null=True,
        blank=True
        )
    birthday=models.DateField(
        'День рождения',
        null=True,
        blank=True
        )
    dateofreg=models.DateTimeField(
        'date joined',
        auto_now_add=True
        )
    avatar=models.ImageField(
        'Аватар',
        upload_to='user/avatars/',
        null=True,
        blank=True
        )
    is_admin = models.BooleanField(
        'Суперпользователь',
        default=False
    )
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
	
    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
