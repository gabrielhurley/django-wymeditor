================
Django WYMEditor
================

A Django application that contains a widget to render a form field with a
WYMEditor_ interface.

 .. _WYMEditor: http://www.wymeditor.org/

Requirements
============

Currently integration with django-filebrowser is hard-coded in. This will
be fixed in a future version. For now, make sure you have django-filebrowser
installed and included in your ``INSTALLED_APPS``, and that the the following
line is in your URLconf::

    (r'^admin/filebrowser/', include('filebrowser.urls')),

With that, you should have full filebrowser integration w/ WYMEditor.