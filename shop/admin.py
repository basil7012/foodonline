from django.contrib import admin
from . models import *

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,catadmin)


class prodadmin(admin.ModelAdmin):

    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(products,prodadmin)



# Register your models here.
