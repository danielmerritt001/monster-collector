from django.contrib import admin
# import your models here
from .models import Monster, Checklist, Bane

# Register your models here
admin.site.register(Monster)
admin.site.register(Checklist)
admin.site.register(Bane)