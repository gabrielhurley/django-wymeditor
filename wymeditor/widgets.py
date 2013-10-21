from django import forms
from django.conf import settings
from django.contrib.admin import widgets

class WYMEditorArea(forms.Textarea):
    def __init__(self, attrs={}, protocol='http'):
        base_class = attrs.get("class", "")
        attrs['class'] = " ".join((base_class, "WYMEditor",))
        self.protocol = protocol
        super(WYMEditorArea, self).__init__(attrs=attrs)

    def _media(self):
        css = {
            "all": (
                "%s://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/smoothness/jquery-ui.css" % self.protocol,
                '%swymeditor/skins/twopanels/skin.css' % settings.STATIC_URL,
            )
        }
        js = (
            '%s://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js' % self.protocol,
            '%swymeditor/jquery.wymeditor.js' % settings.STATIC_URL,
            '%swymeditor/plugins/embed/jquery.wymeditor.embed.js' % settings.STATIC_URL,
            '%sjs/load_wymeditor.js' % settings.STATIC_URL,
        )

        return forms.Media(css=css, js=js)

    media = property(_media)

class AdminWYMEditorArea(widgets.AdminTextareaWidget, WYMEditorArea):
    pass
