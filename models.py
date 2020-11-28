from django.db import models


# Create your models here.


class techer(models.Model):
    post_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.teacher_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
select_course =( ('IIT-JEE','IIT-JEE'),('NEET','NEET'),('CIVIL-SERVICE','CIVIL-SERVICE'),('OTHER-GOVERMENT JOBS','OTHER-GOVERMENT JOBS'))

class student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    courses = models.CharField(max_length=20, choices=select_course)
    userid = models.CharField(max_length=30, unique=True)
    passwd = models.CharField(max_length=30)

    class Meta:
        db_table = 'student'
