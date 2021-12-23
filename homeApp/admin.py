from django.contrib import admin
from homeApp.models import SlideModel, Skill

# Register your models here.
class SlideModelAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'short_des',
        'slide_image'
    ]
admin.site.register(SlideModel, SlideModelAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'skill_title',
        'skill_Quantity'
    ]
admin.site.register(Skill, SkillAdmin)