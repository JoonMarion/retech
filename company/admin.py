from django.contrib import admin
from sklearn.linear_model import ARDRegression
from .models import Company, Address

# Register your models here.
admin.site.register(Company)
admin.site.register(Address)
