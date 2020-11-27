from django.contrib import admin

from ads.models import Ad, Comment

# Register your models here.

class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')

admin.site.register(Ad, PicAdmin)
admin.site.register(Comment)
