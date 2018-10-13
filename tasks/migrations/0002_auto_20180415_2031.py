# Generated by Django 2.0.2 on 2018-04-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='timing',
            field=models.FloatField(blank=True, default=1.313747546987002e-05, null=True, verbose_name='Время затраченное на эксперимент'),
        ),
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.FloatField(blank=True, default=0.013809128903267126, null=True, verbose_name='Время попадания на страницу'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='answerTime',
            field=models.FloatField(blank=True, default=0.01439826256886911, null=True, verbose_name='Время ответа'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='time',
            field=models.FloatField(blank=True, default=0.014410578952122112, null=True, verbose_name='Затраченное время'),
        ),
    ]
