from django.contrib import admin

from wymeditor.models import WYMEditorField
from wymeditor.widgets import AdminWYMEditorArea

class WYMAdmin(admin.ModelAdmin):
    formfield_overrides = {
        WYMEditorField: {'widget': AdminWYMEditorArea},
    }