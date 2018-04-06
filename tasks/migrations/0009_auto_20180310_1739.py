# Generated by Django 2.0.2 on 2018-03-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20180309_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(default='', max_length=6, verbose_name='Ваш Ответ ')),
                ('check', models.CharField(default='Не решено', max_length=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='variant',
        ),
        migrations.AddField(
            model_name='variant',
            name='variant_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
