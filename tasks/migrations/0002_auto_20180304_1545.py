# Generated by Django 2.0.2 on 2018-03-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='lev_user',
        ),
        migrations.AddField(
            model_name='task',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='strategy',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='answer',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='task',
            name='quest',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Experiment'),
        ),
        migrations.AlterField(
            model_name='task',
            name='variant',
            field=models.CharField(max_length=6),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
