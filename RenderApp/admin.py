from django.contrib import admin
from .models import Fornecedor,Empresa,Interesse,Apoiadores,Newsletter

# Register your models here.
admin.site.register(Fornecedor)
admin.site.register(Empresa)
admin.site.register(Interesse)
admin.site.register(Apoiadores)
admin.site.register(Newsletter)