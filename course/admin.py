from django.contrib import admin

# Register your models here.
from .models import techer, Contact, student

admin.site.register(techer)
admin.site.register(Contact)
admin.site.register(student)

