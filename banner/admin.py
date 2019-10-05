from django.contrib import admin

from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'ftext')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

    search_fields = ["title"]

admin.site.register(Banner, BannerAdmin)
# Register your models here.
