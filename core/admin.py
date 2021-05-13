from django.contrib import admin
from .models import AboutPage, IndexPage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['id', ]
    list_display_links = ['id', ]


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'url')}),
        ('Methods', {'description': 'Select that applies', 'fields': (
            'has_get', 'has_post', 'has_put', 'has_patch', 'has_delete')})
    )
    list_display = ['id', 'title', 'has_get',
                    'has_post', 'has_put', 'has_patch', 'has_delete']
    list_display_links = ['id', 'title']
