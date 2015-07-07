from django.contrib import admin
from models import Page, PageTranslation

class PageAdmin(admin.ModelAdmin):
    exclude = ['posted']
    #fields = ['posted', 'title']
    list_display = ('title', 'posted', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class PageTranslationAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'page')
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
admin.site.register(PageTranslation, PageTranslationAdmin)
