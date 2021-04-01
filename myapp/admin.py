from django.contrib import admin
from .models import Account,Data

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','account']


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','photo','account_type','current_status']