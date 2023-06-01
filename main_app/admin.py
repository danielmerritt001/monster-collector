from django.contrib import admin
# import your models here
from .models import Monster, Checklist

# Register your models here
admin.site.register(Monster)
admin.site.register(Checklist)