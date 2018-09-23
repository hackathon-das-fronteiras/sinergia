# Generated by Django 2.0 on 2018-09-23 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100, verbose_name='Nome da Empresa')),
                ('cnpj', models.CharField(max_length=50, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Endereço')),
                ('telefone', models.CharField(max_length=13, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('telefone', models.CharField(max_length=10, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('residuos', models.CharField(max_length=100, verbose_name='Resíduos')),
                ('tipo_residuos', models.CharField(max_length=100, verbose_name='Tipo de Resíduos')),
                ('volume_produto', models.CharField(max_length=30, verbose_name='Volume de Resíduos')),
                ('image', models.ImageField(upload_to='foto_residuo', verbose_name='Imagem Resíduo')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Endereço')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RenderApp.Fornecedor')),
            ],
        ),
    ]