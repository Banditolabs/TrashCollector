from django.contrib import admin

# Register your models here.
from .models import Trash, Feeding

admin.site.register(Trash)
admin.site.register(Feeding)

