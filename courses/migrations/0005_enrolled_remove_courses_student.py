# Generated by Django 4.0.5 on 2022-06-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_courses_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.IntegerField()),
                ('studentname', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='courses',
            name='student',
        ),
    ]