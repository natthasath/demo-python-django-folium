from django.contrib import admin
from .models import location, group, focus

# Register your models here.
admin.site.register(location)
admin.site.register(group)
admin.site.register(focus)