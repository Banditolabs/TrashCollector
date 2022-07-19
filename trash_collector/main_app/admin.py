from django.contrib import admin

# Register your models here.
from .models import Trash, Feeding,Use

admin.site.register(Trash)
admin.site.register(Feeding)
admin.site.register(Use)

