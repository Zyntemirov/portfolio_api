from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'ftext')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

admin.site.register(Blog, BlogAdmin)
# Register your models here.
