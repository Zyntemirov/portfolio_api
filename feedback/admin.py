from django.contrib import admin

from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('fautor_name', 'ftext')
    save_as = True

    def fautor_name(self, obj):
        return obj.autor_name

    fautor_name.short_description = 'Имя автора'

    def ftext(self, obj):
        return obj.text

    ftext.short_description = 'ОПИСАНИЕ'

admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
