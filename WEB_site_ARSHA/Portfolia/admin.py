from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','descpritions','xozirgi_narx','oldingi_narx','created_one','categpory','mavjudmi','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Portfolia, CategoryAdmin)

admin.site.register(Services)