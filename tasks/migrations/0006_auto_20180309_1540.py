# Generated by Django 2.0.2 on 2018-03-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20180309_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='variant',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Ваш Ответ '),
        ),
    ]
