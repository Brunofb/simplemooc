import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin, UserManager)


class User(AbstractBaseUser, PermissionsMixin):
    # Classe de usuario padrao Django

    username = models.CharField(
        'Nome do usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile(
            '^[\w.@+-]+$'),
            'O nome de usuário só pode conter os seguintes caracteres:'
            ' @/./+/_', 'invalid')])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome completo', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', default=True, blank=True)
    is_staff = models.BooleanField('É da equipe?', default=False, blank=True)
    date_joined = models.DateTimeField('Data de criação', auto_now_add=True)

    obejects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    @models.permalink
    def get_absolute_url(self):
        return ('')
