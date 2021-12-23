from django.contrib import admin
from homeApp.models import SlideModel, Skill, Services, Appoinment, Department, Department_galary


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


class ServidesAdmin(admin.ModelAdmin):
    list_display = [
        'service_title',
        'service_des',
    ]
admin.site.register(Services, ServidesAdmin)


class AppoinmentAdmin(admin.ModelAdmin):
    list_display = [
        'f_name',
        'l_name',
        'subject',
        'appointment_date',
        'email',
        'phone',
        'message',
    ]
admin.site.register(Appoinment, AppoinmentAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'dep_name',
        'slug',
    ]
    prepopulated_fields = {'slug': ('dep_name',)}

admin.site.register(Department, DepartmentAdmin)


class Department_gal_Admin(admin.ModelAdmin):
    list_display = [
        'department',
        'dep_title',
        'dep_sub_title',
        'dep_image',
    ]
    
admin.site.register(Department_galary, Department_gal_Admin)
