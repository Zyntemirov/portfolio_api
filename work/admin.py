from django.contrib import admin

from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'ftext')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

admin.site.register(Work, WorkAdmin)
# Register your models here.
