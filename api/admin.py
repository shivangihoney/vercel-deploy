from django.contrib import admin
from .models import company
# Register your models here.

@admin.register(company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'com_name', 'email_id']