from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.EmailField(max_length=255, blank=False, verbose_name='E-mail')
    senha = models.CharField(max_length=255, verbose_name='Senha')




