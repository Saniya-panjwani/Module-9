from django.contrib import admin
from .models import Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization','experience','city')
    search_fields = ('name','specialization')
list_filter = ('specialization','city')

admin.site.register(Doctor,DoctorAdmin)