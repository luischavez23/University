# Generated by Django 4.1.2 on 2022-11-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_course_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='id_course',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
