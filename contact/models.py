from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
    first_name = models.CharField(max_length=50, verbose_name='Primeiro nome')
    last_name = models.CharField(
        max_length=50, blank=True, verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(
        max_length=254, blank=True, verbose_name='E-mail')
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Data de criação')
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True, verbose_name='Exibir')
    picture = models.ImageField(
        upload_to='pictures/%Y/%m', blank=True, verbose_name='Imagem')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name='Categoria')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name='Usuário')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
