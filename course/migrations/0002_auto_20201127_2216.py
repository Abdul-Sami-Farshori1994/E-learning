# Generated by Django 2.2.10 on 2020-11-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('IIT-JEE', 'IIT-JEE'), ('NEET', 'NEET'), ('CIVIL-SERVICE', 'CIVIL-SERVICE'), ('OTHER-GOVERMENT JOBS', 'OTHER-GOVERMENT JOBS')], max_length=20),
        ),
    ]
