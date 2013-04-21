# import models
# from django.contrib import admin
# # from wiki.models import Page

# class PageAdmin(admin.ModelAdmin):


# admin.site.register(models.Page, PageAdmin)




from wiki.models import Page
from django.contrib import admin
 
admin.site.register(Page)