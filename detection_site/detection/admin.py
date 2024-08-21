from django.contrib import admin
from .models import Det_model, Det_result

class DetectAdmin_before(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Det_model, DetectAdmin_before)

class DetectAdmin_after(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Det_result, DetectAdmin_after)
