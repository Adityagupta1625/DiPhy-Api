# Generated by Django 4.0.5 on 2022-06-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='student',
        ),
        migrations.AddField(
            model_name='courses',
            name='student',
            field=models.ManyToManyField(blank=True, to='student.student'),
        ),
    ]
