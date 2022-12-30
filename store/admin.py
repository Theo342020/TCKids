from django.contrib import admin
from .models import Clothes

# Register your models here.
class imageAdmin(admin.ModelAdmin):
	list_display = ["description", "manufacturer", "gender", "quantity", "price", "size", "picture"]

admin.site.register(Clothes, imageAdmin)
