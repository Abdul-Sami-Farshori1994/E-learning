# Generated by Django 2.2.10 on 2020-11-27 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20201127_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='courses',
        ),
    ]
