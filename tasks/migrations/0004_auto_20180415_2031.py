# Generated by Django 2.0.2 on 2018-04-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20180415_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='startTime',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='Время начала эксперимента'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='timing',
            field=models.FloatField(blank=True, default=1.2726929361436583e-05, null=True, verbose_name='Время затраченное на эксперимент'),
        ),
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.FloatField(blank=True, default=0.013845667506917701, null=True, verbose_name='Время попадания на страницу'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='answerTime',
            field=models.FloatField(blank=True, default=0.014446296463555821, null=True, verbose_name='Время ответа'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='time',
            field=models.FloatField(blank=True, default=0.01445902339291726, null=True, verbose_name='Затраченное время'),
        ),
    ]
