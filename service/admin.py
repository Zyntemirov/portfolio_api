from django.contrib import admin

from .models import Service, Success

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'ftext')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

class SuccessAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'ftext')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

admin.site.register(Service, ServiceAdmin)
admin.site.register(Success, SuccessAdmin)
# Register your models here.
