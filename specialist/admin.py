from django.contrib import admin

from .models import Specialist, Skill

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('ftitle', 'fdescription')
    save_as = True

    def ftitle(self, obj):
        return obj.title

    ftitle.short_description = 'НАЗВАНИЕ'

    def fdescription(self, obj):
        return obj.description

    fdescription.short_description = 'ОПИСАНИЕ'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('fname', 'flevel')
    save_as = True

    def fname(self, obj):
        return obj.name

    fname.short_description = 'НАЗВАНИЕ'

    def flevel(self, obj):
        return obj.level

    flevel.short_description = 'Уровень'

admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Skill, SkillAdmin)
# Register your models here.
