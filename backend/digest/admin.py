from django.contrib import admin

from .models import Digest


class DigestAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('user',  'created_at')
    search_fields = ('user',  'created_at')
    list_filter = ('user',  'created_at')


admin.site.register(Digest, DigestAdmin)
