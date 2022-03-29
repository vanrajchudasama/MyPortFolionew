from django.contrib import admin
from .models import Contact_Us


@admin.register(Contact_Us)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']
    search_fields =['name','email','subject','message']