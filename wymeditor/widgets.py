from django import forms
from django.conf import settings
from django.contrib.admin import widgets

class WYMEditorArea(forms.Textarea):
    def __init__(self, attrs={}):
        base_class = attrs.get("class", "")
        attrs['class'] = " ".join((base_class, "WYMEditor",))
        super(WYMEditorArea, self).__init__(attrs=attrs)

    class Media:
        css = {
            "all": (
                "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/smoothness/jquery-ui.css",
                '%swymeditor/skins/twopanels/skin.css' % settings.STATIC_URL,
            )
        }
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js',
            '%swymeditor/jquery.wymeditor.js' % settings.STATIC_URL,
            '%sjs/load_wymeditor.js' % settings.STATIC_URL,
        )

class AdminWYMEditorArea(widgets.AdminTextareaWidget, WYMEditorArea):
    pass
