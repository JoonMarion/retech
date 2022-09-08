import os
from utils import *
from django.db import models

class Company(models.Model):
    class Meta:
        verbose_name_plural = "Company's"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(blank=True)
    cnpj = models.CharField(max_length=14, null=True)
    address = models.OneToOneField('Address', on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=11, null=True)
    logo = models.ImageField(upload_to=upload_logo_formatter, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def has_logo(self):
        return True if self.logo.name else False

    def remove_logo(self):
        if self.has_logo():
            if os.path.isfile(self.logo.path):
                os.remove(self.logo.path)
            self.logo = None

    def edit_logo(self, pk, Logo):
        logo = Company.objects.get(id=pk)
        logo.remove_logo()
        logo.logo = Logo

    def save(self, *args, **kwargs):
        if self.id:
            old_obj = Company.objects.get(id=self.id)
            if old_obj.logo != self.logo:
                self.edit_logo(self.id, self.logo)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.remove_logo()
        super().delete(*args, **kwargs)


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Address's"

    street = models.CharField(max_length=100)
    number = models.IntegerField()
    district = models.CharField(max_length=100, null=True)
    complement = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    cep = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.street + ', ' + str(self.number) + ', ' + self.city + ' - ' + self.state 