from django.contrib import admin
from homeApp.models import SlideModel

# Register your models here.
class SlideModelAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'short_des',
        'slide_image'
    ]
    summernote_fields = ('discription',)

admin.site.register(SlideModel, SlideModelAdmin)
