from django.contrib import admin
from .models import message, QuillPost
# Register your models here.

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(message)
