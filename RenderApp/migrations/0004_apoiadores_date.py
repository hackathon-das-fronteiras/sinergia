# Generated by Django 2.0 on 2018-09-23 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RenderApp', '0003_apoiadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='apoiadores',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data registro'),
        ),
    ]