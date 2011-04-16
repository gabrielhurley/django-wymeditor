from django.conf import settings
from django.db import models

from wymeditor.widgets import WYMEditorArea

class WYMEditorField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': WYMEditorArea}
        defaults.update(kwargs)
        return super(WYMEditorField, self).formfield(**defaults)

if 'south' in settings.INSTALLED_APPS
    from south.modelsinspector import add_introspection_rules
        add_introspection_rules([], ["^wymeditor\.models\.WYMEditorField"])